# -*- mode: python ; coding: utf-8 -*-
# для сборки с помощью pyinstaller(очень медленно)
block_cipher = None

a = Analysis(['ryton_launcher.py'],
             pathex=[],
             binaries=[],
             datas=[
                 ('Interpritator', 'Interpritator'),
                 ('Interpritator/std', 'Interpritator/std'),
                 ('Interpritator/std/lib', 'Interpritator/std/lib'),
                 ('Interpritator/std/Terminal.py', 'Interpritator/std'),
                 ('Interpritator/std/JITCompiler.py', 'Interpritator/std'),
                 ('Interpritator/std/RuVix.py', 'Interpritator/std'),
                 ('Interpritator/std/Path.py', 'Interpritator/std'),
                 ('Interpritator/std/Files.py', 'Interpritator/std'),
                 ('Interpritator/std/String.py', 'Interpritator/std'),
                 ('Interpritator/std/DateTime.py', 'Interpritator/std'),
                 ('Interpritator/std/Archive.py', 'Interpritator/std'),
                 ('Interpritator/std/DeBugger.py', 'Interpritator/std'),
                 ('Interpritator/std/ErroRize.py', 'Interpritator/std'),
                 ('Interpritator/std/ParallelComputing.py', 'Interpritator/std'),
                 ('Interpritator/std/BigNumMath.py', 'Interpritator/std'),
                 ('Interpritator/std/RuVixCore.py', 'Interpritator/std'),
                 ('Interpritator/std/Algorithm.py', 'Interpritator/std'),
                 ('Interpritator/std/HyperConfigFormat.py', 'Interpritator/std'),
                 ('Interpritator/std/System.py', 'Interpritator/std'),
                 ('Interpritator/std/DocTools.py', 'Interpritator/std'),
                 ('Interpritator/std/RuVix/RuVixApp.py', 'Interpritator/std/RuVix'),
                 ('Interpritator/std/RuVix/RuVixGame.py', 'Interpritator/std/RuVix'),
                 ('Interpritator/std/RuVix/RuVixEffects.py', 'Interpritator/std/RuVix'),
                 ('Interpritator/std/MatplotUp.py', 'Interpritator/std'),
                 ('Interpritator/std/RuVixEffects.py', 'Interpritator/std'),
                 ('Interpritator/std/NeuralNet.py', 'Interpritator/std'),
                 ('Interpritator/std/Media.py', 'Interpritator/std'),
                 ('Interpritator/std/NetWorker.py', 'Interpritator/std'),
                 ('Interpritator/std/Tuix.py', 'Interpritator/std'),
                 ('Interpritator/std/MetaTable.py', 'Interpritator/std'),
                 ('Interpritator/std/ColoRize.py', 'Interpritator/std'),
                 ('Interpritator/std/RunTimer.py', 'Interpritator/std'),
                 ('Interpritator/std/RuiX.py', 'Interpritator/std'),
                 ('Interpritator/std/DSL.py', 'Interpritator/std'),
                 ('Interpritator/std/ProgRessing.py', 'Interpritator/std'),
                 ('Interpritator/stdFunction.py', 'Interpritator'),
                 ('Interpritator/Core.py', 'Interpritator'),
                 ('Interpritator/SyntaxTransformer.py', 'Interpritator'),
                 ('Interpritator/ErrorHandler.py', 'Interpritator'),
                 ('Interpritator/Effects.py', 'Interpritator'),
                 ('Interpritator/Pragma.py', 'Interpritator'),
                 ('Interpritator/MemoryManager.py', 'Interpritator'),
                 ('Interpritator/PackageSystem.py', 'Interpritator')
             ],
             hiddenimports=[
                 # Внешние зависимости
                 'aiosignal', 'altgraph', 'attrs', 'certifi', 'charset_normalizer',
                 'click', 'cloudpickle', 'Cython', 'dask', 'filelock', 'frozenlist',
                 'fsspec', 'idna', 'jsonschema', 'jsonschema_specifications', 'llvmlite',
                 'locket', 'markdown_it_py', 'mdurl', 'msgpack', 'numba', 'numpy',
                 'packaging', 'partd', 'protobuf', 'psutil', 'pyfiglet', 'Pygments',
                 'PyYAML', 'ray', 'referencing', 'requests', 'rich', 'rpds_py',
                 'toolz', 'urllib3',
                 
                 # Стандартная библиотека Ryton
                 'Interpritator.std.Terminal',
                 'Interpritator.std.JITCompiler',
                 'Interpritator.std.RuVix',
                 'Interpritator.std.Path',
                 'Interpritator.std.Files',
                 'Interpritator.std.String',
                 'Interpritator.std.DateTime',
                 'Interpritator.std.Archive',
                 'Interpritator.std.DeBugger',
                 'Interpritator.std.ErroRize',
                 'Interpritator.std.ParallelComputing',
                 'Interpritator.std.BigNumMath',
                 'Interpritator.std.RuVixCore',
                 'Interpritator.std.Algorithm',
                 'Interpritator.std.HyperConfigFormat',
                 'Interpritator.std.System',
                 'Interpritator.std.DocTools',
                 'Interpritator.std.RuVix.RuVixApp',
                 'Interpritator.std.RuVix.RuVixGame',
                 'Interpritator.std.RuVix.RuVixEffects',
                 'Interpritator.std.MatplotUp',
                 'Interpritator.std.RuVixEffects',
                 'Interpritator.std.NeuralNet',
                 'Interpritator.std.Media',
                 'Interpritator.std.NetWorker',
                 'Interpritator.std.Tuix',
                 'Interpritator.std.MetaTable',
                 'Interpritator.std.lib',
                 'Interpritator.std.ColoRize',
                 'Interpritator.std.RunTimer',
                 'Interpritator.std.RuiX',
                 'Interpritator.std.DSL',
                 'Interpritator.std.ProgRessing',
                 
                 # Ядро Ryton
                 'Interpritator.stdFunction',
                 'Interpritator.Core',
                 'Interpritator.SyntaxTransformer',
                 'Interpritator.ErrorHandler',
                 'Interpritator.Effects',
                 'Interpritator.Pragma',
                 'Interpritator.MemoryManager',
                 'Interpritator.PackageSystem'
             ],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='ryton',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True)
