from typing import List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
    async def connect(self, websocket: WebSocket):
        if len(self.active_connections)>=2:
            await websocket.accept()
            await websocket.close(4000)
        else:
            await websocket.accept()
            self.active_connections.append(websocket)
            if len(self.active_connections)==1:
                await websocket.send_json({
                    'stage': 'init',
                    'players_count': len(self.active_connections),
                    'self': 'X'
                })
            else:
                await websocket.send_json({
                    'stage': 'init',
                    'players_count': len(self.active_connections),
                    'self': 'O'
                })
                await self.active_connections[0].send_json({
                    'stage': 'init',
                    'players_count': len(self.active_connections),
                    'self': 'X'
                })
    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
    async def broadcast(self, data: str):
        for connection in self.active_connections:
            await connection.send_json(data)

def init_board():
    return [
        None, None, None,
        None, None, None,
        None, None, None
    ]

def update_board(data):
    global board
    board[int(data["cell"])-1] = data["player"]

def is_won():
    global board
    return (
        board[0] == board[1] == board[2] != None or
        board[3] == board[4] == board[5] != None or
        board[6] == board[7] == board[8] != None or
        board[0] == board[4] == board[8] != None or
        board[2] == board[4] == board[6] != None or
        board[0] == board[3] == board[6] != None or
        board[1] == board[4] == board[7] != None or
        board[2] == board[5] == board[8] != None 
    )

def is_draw():
    global board
    for cell in board:
        if not cell:
            return False
    return True

manager = ConnectionManager()
board = init_board()
swapper = {
    'X': 'O',
    'O': 'X'
}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            global board
            response = await websocket.receive_json()
            update_board(response)
            if  is_won():
                data={
                    'stage': 'end',
                    'winner': response['player'],
                    'current_player': '',
                    'cell': response['cell'],
                    'sign': response['player']
                }
                # manager.disconnect(websocket)
                # board = init_board()
            elif is_draw():
                data={
                    'stage': 'end',
                    'winner': 'friendship',
                    'current_player': '',
                    'cell': response['cell'],
                    'sign': response['player']
                }
                # manager.disconnect(websocket)
                # board = init_board()
            else:
                data = {
                    'stage': 'active',
                    'current_player': swapper[response['player']],
                    'cell': response['cell'],
                    'sign': response['player']
                }
            await manager.broadcast(data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
    except:
        pass

@app.get("/reg")
async def reg():
    
    return 