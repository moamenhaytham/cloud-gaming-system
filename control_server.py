import asyncio
import websockets
import json
import pyautogui
import keyboard

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False

KEY_MAP = {
    'Control': 'ctrl', 'Alt': 'alt', 'Shift': 'shift',
    'Enter': 'enter', 'Tab': 'tab', 'Escape': 'esc',
    'Backspace': 'backspace', 'Delete': 'delete', 
    ' ': 'space',
    'ArrowUp': 'up', 'ArrowDown': 'down', 
    'ArrowLeft': 'left', 'ArrowRight': 'right',
    'CapsLock': 'capslock', 'PageUp': 'pageup', 
    'PageDown': 'pagedown', 'Home': 'home', 'End': 'end'
}

async def handler(websocket):
    print("🎮 عميل متصل من الخارج!")
    
    try:
        async for message in websocket:
            try:
                data = json.loads(message)
                cmd = data.get('type')
                
                if cmd == 'mousemove':
                    x, y = data['x'], data['y']
                    pyautogui.moveTo(x, y, duration=0)
                    
                elif cmd == 'mousedown':
                    button = data.get('button', 'left')
                    pyautogui.mouseDown(button=button)
                    
                elif cmd == 'mouseup':
                    button = data.get('button', 'left')
                    pyautogui.mouseUp(button=button)
                    
                elif cmd == 'scroll':
                    delta = data.get('delta', 0)
                    pyautogui.scroll(int(delta / 100))
                    
                elif cmd == 'keydown':
                    key = data.get('key', '')
                    if key:
                        key = KEY_MAP.get(key, key.lower())
                        keyboard.press(key)
                        
                elif cmd == 'keyup':
                    key = data.get('key', '')
                    if key:
                        key = KEY_MAP.get(key, key.lower())
                        keyboard.release(key)
                        
            except Exception as e:
                print(f"❌ خطأ في الأمر: {e}")
                
    except Exception as e:
        print(f"🔌 العميل انقطع: {e}")

async def main():
    server = await websockets.serve(handler, "0.0.0.0", 8765)
    print("✅ خادم التحكم شغال على البورت 8765")
    print("🌍 جاهز لاستقبال اتصالات من الخارج")
    await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())