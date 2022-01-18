from types import SimpleNamespace
from src.utils.keyboard import create_keyboard


keys = SimpleNamespace(
    settings='Setting :gear:',
    random_connect='Connect :handshake:',
    help='Help :smiling_face_with_halo:')
    
keyboards = SimpleNamespace(
    main_keyboard=create_keyboard(keys.random_connect, keys.settings,
    keys.help)
)