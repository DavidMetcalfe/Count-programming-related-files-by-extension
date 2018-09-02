
import os

# Dictionary containing languages and associated extensions.
d = {'A♯ (Axiom)': ['.as'], 'ActionScript': ['.as'], 'Ada': ['.adb', '.ads'], 'Agda': ['.agda', '.lagda'], 'Aldor': ['.al', '.as'], 'AmbientTalk': ['.at'], 'AMPL': ['.mod', '.dat', '.run'], 'AppleScript': ['.scpt', '.scptd', '.applescript'], 'AspectJ': ['aj'], 'B': ['.b'], 'Batch file': ['.bat', '.cmd', '.btm'], 'C': ['.c', '.h'], 'C++': ['.C', '.cc', '.cpp', '.cxx', '.c++', '.h', '.hh', '.hpp', '.hxx', '.h++'], 'C Sharp': ['.cs'], 'Ceylon': ['.ceylon'], 'Chapel': ['.chpl'], 'Citrine': ['ctr'], 'Claire': ['.cl'], 'Clean': ['.icl', '.dcl', '.abc', '.sapl'], 'Clojure': ['.clj', '.cljs', '.cljc', '.edn'], 'COBOL': ['.cbl', '.cob', '.cpy'], 'Cobra': ['.cobra'], 'CoffeeScript': ['.coffee', '.litcoffee'], 'Common Lisp': ['.lisp', '.lsp', '.l', '.cl', '.fasl'], 'Crystal': ['.cr'], 'Cuneiform': ['.cfl'], 'D': ['.d'], 'Dart': ['.dart'], 'Darwin': ['.drw'], 'Object Pascal': ['.p', '.pp', '.pas'], 'eC': ['.ec', '.eh'], 'Eiffel': ['.e'], 'Elixir': ['.ex', '.exs'], 'Elm': ['.elm'], 'Emacs Lisp': ['.el', '.elc'], 'Erlang': ['.erl', '.hrl'], 'Euphoria': ['.e', '.ex', '.exw', '.edb'], 'F Sharp': ['.fs', '.fsi', '.fsx', '.fsscript'], 'Falcon': ['.ftd', '.fal', '.fam'], 'Fantom': ['.fan', '.fwt', '.pod'], 'Fjölnir': ['.fjo', '.fjv', '.sma', '.ein'], 'Fortran': ['.f', '.for', '.f90'], 'G': ['.mpt', '.mpf', '.nc'], 'Genie': ['.gs'], 'Go': ['.go'], 'Gosu': ['.gs', '.gsp', '.gst', '.gsx'], 'Apache Groovy': ['.groovy'], 'Harbour': ['.prg', '.ch', '.hb', '.hbp'], 'Haskell': ['.hs', '.lhs'], 'Haxe': ['.hx', '.hxml'], 'Idris': ['.idr', '.lidr'], 'J#': ['.jsl'], 'Java': ['.java', '.class', '.jar'], 'JavaScript': ['.js', '.mjs'], 'JScript': ['.js', '.jse', '.wsf', '.wsc'], 'Julia': ['.jl'], 'Kojo': ['.kojo'], 'Kotlin': ['.kt', '.kts'], 'Lasso': ['.lasso', '.LassoApp'], 'LiveScript': ['.ls'], 'Lua': ['.lua'], 'Mercury': ['.m'], 'MetaQuotes Language MQL4/MQL5': ['.ex4', '.mq4', '.mqh', '.ex5', '.mq5'], 'MIVA Script': ['.mv', '.mvc', '.mvt'], 'Modula-2': ['.mod', '.m2', '.def', '.mi', '.md'], 'mIRC scripting language': ['.mrc'], 'Neko': ['.neko', '.n'], 'Nemerle': ['.n'], 'NetLogo': ['.nlogo', '.nlogo3d', '.nls'], 'NetRexx': ['.nrx'], 'Nim': ['.nim'], 'Object REXX': ['.rxs', '.rex'], 'Objective-C': ['.h', '.m', '.mm'], 'OCaml': ['.ml', '.mli'], 'P': ['.p'], 'P4': ['.p4'], 'ParaSail': ['.psi', '.psl'], 'Pascal': ['.pp', '.pas', '.inc'], 'Perl': ['.pl', '.pm', '.t', '.pod'], 'Perl 6': ['.p6', '.pl6', '.pm6', '.pm'], 'PHP': ['.php', '.phtml', '.php3', '.php4', '.php5', '.php7', '.phps', '.php-s', '.pht'], 'PicoLisp': ['.l'], 'Programming Language for Business': ['.rl', '.ps', '.cb'], 'PowerShell': ['.ps1', '.ps1xml', '.psc1', '.psd1', '.psm1', '.pssc', '.cdxml'], 'Processing': ['.pde'], 'Prolog': ['.pl', '.pro', '.P'], 'PROMAL': ['.s'], 'ProvideX': ['.pvx', '.pvc', '.pvk', '.pvt'], 'PureBasic': ['.pb', '.pbi', '.pbf', '.pbp', '.pbv'], 'Python': ['.py', '.pyc', '.pyd', '.pyo', '.pyw', '.pyz'], 'Q Sharp': ['.qs'], 'R': ['.r', '.rdata', '.rds', '.rda'], 'Racket': ['.rkt', '.rktl', '.rktd', '.scrbl', '.plt', '.ss', '.scm'], 'Rebol': ['.r', '.reb'], 'Red': ['.red', '.reds'], 'REXX': ['.cmd', '.bat', '.exec', '.rexx', '.rex'], 'Ring': ['.ring', '.rh', '.rform'], 'Ruby': ['.rb'], 'Rust': ['.rs', '.rlib'], 'SALSA': ['.salsa'], 'Scala': ['.scala', '.sc'], 'Scheme': ['.scm', '.ss'], 'Seed7': ['.sd7', '.s7i'], 'Scratch': ['.scratch', '.sb', '.sprite', '.sb2', '.sprite2'], 'Standard ML': ['.sml'], 'Snap!': ['.ypr', '.ysp'], 'Squirrel': ['.nut'], 'Swift': ['.swift'], 'SystemVerilog': ['.sv'], 'Tcl': ['.tcl', '.tbc'], 'TOM (object': ['.t'], 'TypeScript': ['.ts', '.tsx'], 'Umple': ['.ump'], 'UnrealScript': ['.uc', '.uci', '.upkg'], 'Vala': ['.vala', '.vapi'], 'Verilog': ['.v'], 'Visual Basic .NET': ['.vb'], 'Wolfram Language': ['.nb', '.m', '.wl'], 'X10': ['.x10'], 'XC': ['.xc'], 'XQuery': ['.xq', '.xql', '.xqm', '.xqy', '.xquery'], 'XSB': ['.p'], 'Yorick': ['.i']}

# Create second dictionary only containing language names.
dd = {}
for i in d.keys():
    dd[i] = 0

# Temporary dictionary
tmp = {}

# Get directory path of this script.
rootdir = os.path.dirname(__file__)

def getScriptName():
    '''Get the filename of this script.'''
    import os.path
    return os.path.splitext(os.path.basename(__file__))[0]

def getExtension(path):
    '''Return file extension of inputted path.'''
    return os.path.splitext(path)[1]

# Loop through files in rootdir, add counts to tmp dict.
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        ext = getExtension(file).lower()
        if ext in tmp:
            tmp[ext] += 1
        else:
            tmp[ext] = 1

# Compare items in d with tmp, add counts of matches to dd.
for k, v in d.items():
  for l, m in tmp.items():
    if l in v or l == v:
        try:
            dd[k] += m
        except:
            dd[k] = m

# Output result to txt file with empty values removed.
with open("{} output.txt".format(getScriptName()), "w", encoding='utf-8') as f:
    f.write("{}".format({k: v for k, v in dd.items() if v is not 0}))