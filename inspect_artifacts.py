from pathlib import Path
import pickle, json, binascii, gzip, zipfile, os

root = Path('C:/ANN Classification')
files = ['label_encoder_gender.pk1', 'onehot_encoder_geo.pk1', 'scaler.pk1', 'model.h5']

for name in files:
    path = root / name
    data = path.read_bytes()
    print(f'=== {name} ===')
    print('exists:', path.exists())
    print('size:', len(data))
    print('first 32 bytes hex:', data[:32].hex())
    print('first 64 bytes repr:', repr(data[:64]))
    print('starts with b"PK"?', data.startswith(b'PK'))
    print('starts with gzip magic?', data.startswith(b'\x1f\x8b'))
    print('starts with pickle protocol?', data.startswith((b'\x80', b'\x93', b'\x94', b'\x95')))
    print()

# Try to load each candidate using pickle and joblib when possible.
for name in ['label_encoder_gender.pk1', 'onehot_encoder_geo.pk1', 'scaler.pk1']:
    path = root / name
    print(f'Trying pickle load for {name}')
    try:
        with open(path, 'rb') as f:
            obj = pickle.load(f)
        print('  pickle load succeeded:', type(obj))
    except Exception as e:
        print('  pickle failed:', repr(e))
    print()
