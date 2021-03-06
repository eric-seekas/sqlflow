# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftORleftANDnonassocLELEGEGTEQNEADD ALERT ALL ALTER AND AS ASC CHAR CONNECT CREATE DELETE DESC DROP EQ EXIT FROM GE GRANT GT HELP ID INDEX INSERT INT INTO IS JDBC KEY LE LIMIT LOAD LT NE NOT NULL NUMBER ON OR OVERWRITE PASSWORD PRIMARY PRINT REGISTER REVOKE SAVE SELECT SET SET SHOW SPARKSQL STRING TABLE TABLES TO TRAIN UPDATE USER VALUES VIEW WHERE start : command\n              | command ';'  command : ddl\n                | dml\n                | utility\n                | nothing  ddl : createtable\n            | createindex\n            | droptable\n            | dropindex\n            | showtables\n            | alerttable\n            | createuser\n            | grantuser\n            | revokeuser  dml : query\n            | insert\n            | delete\n            | update\n            | train\n            | register\n            | load\n            | save\n            | connect\n            | set  utility : exit\n                | print  showtables : SHOW TABLES  createuser : CREATE USER ID PASSWORD STRING grantuser : GRANT power_list ON non_mrelation_list TO non_mrelation_list  revokeuser : REVOKE power_list ON non_mrelation_list FROM non_mrelation_list  power_list : power_list ',' power_type\n                   | power_type   power_type : SELECT\n                    | UPDATE\n                    | INSERT\n                    | DELETE\n                    | PRINT\n                    | ALL\n     alerttable : ALERT TABLE ID ADD attrtype\n                   | ALERT TABLE ID DROP non_mrelation_list  createtable : CREATE TABLE ID '(' non_mattrtype_list ')'  createindex : CREATE INDEX ID '(' ID ')'  droptable : DROP TABLE ID  dropindex : DROP INDEX ID '(' ID ')'  print : PRINT ID  exit : EXIT  query : SELECT non_mselect_clause FROM non_mrelation_list opwhere_clause oplimit_clause opas_clause  insert : INSERT INTO ID VALUES inservalue_list  inservalue_list : '(' non_mvalue_list ')' ',' inservalue_list\n                        | '(' non_mvalue_list ')'  delete : DELETE FROM ID opwhere_clause  update : UPDATE ID SET relattr EQ relattr_or_value opwhere_clause  train : TRAIN non_mselect_clause opas_clause  register : REGISTER non_mselect_clause opas_clause  load : LOAD non_mselect_clause opas_clause  save : SAVE OVERWRITE TABLE opas_clause  connect : CONNECT JDBC opwhere_clause  set : SET non_mselect_clause opas_clause  non_mattrtype_list : attrtype ',' non_mattrtype_list\n                           | attrtype  attrtype : ID type\n                 | ID type '(' NUMBER ')'\n                 | PRIMARY KEY '(' ID ')'  type : INT\n             | CHAR  non_mselect_clause : non_mrelattr_list\n                           | '*'  non_mrelattr_list : relattr ',' non_mrelattr_list\n                          | relattr  relattr : ID '.' ID\n                | ID  non_mrelation_list : relation ',' non_mrelation_list\n                           | relation  relation : ID  opwhere_clause : WHERE non_mcond_list\n                       | nothing  oplimit_clause : LIMIT value\n                        | nothing  opas_clause : AS ID\n                    | nothing  non_mcond_list : non_mcond_list AND non_mcond_list\n                       | non_mcond_list OR  non_mcond_list\n                       | '(' non_mcond_list ')'\n                       | condition  condition : relattr op relattr_or_value\n                  | relattr EQ null_value\n                  | relattr NE null_value  relattr_or_value : relattr\n                         | value  non_mvalue_list : value ',' non_mvalue_list\n                        | value\n                        | null_value ',' non_mvalue_list\n                        | null_value  value : STRING  value : NUMBER  null_value : NULL  op : LT\n           | LE\n           | GT\n           | GE\n           | EQ\n           | NE  nothing : "

_lr_action_items = {';': (
    [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
     22,
     23, 24, 25, 26, 27, 44, 52, 64, 65, 66, 67, 71, 72, 73, 74, 76, 77, 81, 91,
     93,
     95, 96, 97, 98, 99, 100, 102, 110, 111, 114, 115, 116, 118, 120, 121, 122,
     124,
     131, 133, 134, 138, 139, 152, 153, 154, 155, 158, 159, 160, 161, 162, 163,
     165,
     169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 184, 185, 186,
     189,
     195, 196, 197, ],
    [-104, 46, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16,
     -17,
     -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -47, -28, -67, -68, -70,
     -72,
     -104, -104, -104, -104, -104, -46, -44, -104, -59, -81, -54, -55, -56,
     -104,
     -58, -77, -74, -75, -104, -69, -71, -52, -80, -57, -76, -85, -29, -40, -41,
     -104, -49, -62, -65, -66, -42, -43, -45, -30, -73, -31, -104, -79, -95,
     -96,
     -97, -89, -104, -90, -82, -83, -84, -86, -87, -88, -48, -78, -51, -53, -63,
     -64, -50, ]), '$end': (
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
     21,
     22, 23, 24, 25, 26, 27, 44, 46, 52, 64, 65, 66, 67, 71, 72, 73, 74, 76, 77,
     81,
     91, 93, 95, 96, 97, 98, 99, 100, 102, 110, 111, 114, 115, 116, 118, 120,
     121,
     122, 124, 131, 133, 134, 138, 139, 152, 153, 154, 155, 158, 159, 160, 161,
     162,
     163, 165, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 184,
     185,
     186, 189, 195, 196, 197, ],
    [-104, 0, -1, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16,
     -17, -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -47, -2, -28, -67,
     -68,
     -70, -72, -104, -104, -104, -104, -104, -46, -44, -104, -59, -81, -54, -55,
     -56, -104, -58, -77, -74, -75, -104, -69, -71, -52, -80, -57, -76, -85,
     -29,
     -40, -41, -104, -49, -62, -65, -66, -42, -43, -45, -30, -73, -31, -104,
     -79,
     -95, -96, -97, -89, -104, -90, -82, -83, -84, -86, -87, -88, -48, -78, -51,
     -53, -63, -64, -50, ]), 'CREATE': ([0, ], [28, ]),
    'DROP': ([0, 83, ], [29, 108, ]), 'SHOW': ([0, ], [30, ]),
    'ALERT': ([0, ], [31, ]), 'GRANT': ([0, ], [32, ]),
    'REVOKE': ([0, ], [33, ]),
    'SELECT': ([0, 32, 33, 85, ], [34, 56, 56, 56, ]),
    'INSERT': ([0, 32, 33, 85, ], [35, 58, 58, 58, ]),
    'DELETE': ([0, 32, 33, 85, ], [36, 59, 59, 59, ]),
    'UPDATE': ([0, 32, 33, 85, ], [37, 57, 57, 57, ]),
    'TRAIN': ([0, ], [39, ]), 'REGISTER': ([0, ], [40, ]),
    'LOAD': ([0, ], [41, ]), 'SAVE': ([0, ], [42, ]),
    'CONNECT': ([0, ], [43, ]), 'SET': ([0, 70, ], [38, 92, ]),
    'EXIT': ([0, ], [44, ]),
    'PRINT': ([0, 32, 33, 85, ], [45, 60, 60, 60, ]),
    'TABLE': ([28, 29, 31, 75, ], [47, 50, 53, 99, ]),
    'INDEX': ([28, 29, ], [48, 51, ]), 'USER': ([28, ], [49, ]),
    'TABLES': ([30, ], [52, ]),
    'ALL': ([32, 33, 85, ], [61, 61, 61, ]),
    '*': ([34, 38, 39, 40, 41, ], [65, 65, 65, 65, 65, ]),
    'ID': (
        [34, 37, 38, 39, 40, 41, 45, 47, 48, 49, 50, 51, 53, 68, 69,
         84, 86, 87, 88, 89, 92, 94, 101, 103, 104, 106, 107, 108,
         123, 135, 136, 137, 141, 142, 143, 145, 146, 147, 148, 149,
         150, 151, 156, 183, ],
        [67, 70, 67, 67, 67, 67, 77, 78, 79, 80, 81, 82, 83, 90, 91,
         111, 111, 111, 67, 116, 67, 120, 67, 126, 130, 132, 126,
         111, 67, 111, 111, 111, 67, 67, 67, 67, -102, -103, -98,
         -99, -100, -101, 126, 191, ]), 'INTO': ([35, ], [68, ]),
    'FROM': (
        [36, 63, 64, 65, 66, 67, 110, 111, 113, 115, 116, 161, ],
        [69, 87, -67, -68, -70, -72, -74, -75, 137, -69, -71,
         -73, ]), 'OVERWRITE': ([42, ], [75, ]),
    'JDBC': ([43, ], [76, ]), 'ON': (
        [54, 55, 56, 57, 58, 59, 60, 61, 62, 112, ],
        [84, -33, -34, -35, -36, -37, -38, -39, 86, -32, ]), ',': (
        [54, 55, 56, 57, 58, 59, 60, 61, 62, 66, 67, 110, 111, 112, 116, 128,
         152,
         153, 154, 167, 168, 169, 170, 171, 186, 195, 196, ],
        [85, -33, -34, -35, -36, -37, -38, -39, 85, 88, -72, 136, -75, -32, -71,
         156, -62, -65, -66, 187, 188, -95, -96, -97, 192, -63, -64, ]), 'AS': (
        [64, 65, 66, 67, 71, 72, 73, 74, 99, 102, 110, 111, 114, 115, 116, 122,
         124,
         138, 161, 163, 165, 169, 170, 171, 172, 174, 175, 176, 177, 178, 179,
         180,
         185, ],
        [-67, -68, -70, -72, 94, 94, 94, 94, 94, -77, -74, -75, -104, -69, -71,
         -76,
         -85, -104, -73, 94, -79, -95, -96, -97, -89, -90, -82, -83, -84, -86,
         -87,
         -88, -78, ]), '.': ([67, ], [89, ]),
    'EQ': ([67, 116, 119, 125, ], [-72, -71, 141, 146, ]),
    'NE': ([67, 116, 125, ], [-72, -71, 147, ]),
    'LT': ([67, 116, 125, ], [-72, -71, 148, ]),
    'LE': ([67, 116, 125, ], [-72, -71, 149, ]),
    'GT': ([67, 116, 125, ], [-72, -71, 150, ]),
    'GE': ([67, 116, 125, ], [-72, -71, 151, ]), 'WHERE': (
        [67, 76, 91, 110, 111, 114, 116, 161, 169, 170, 172, 173, 174, ],
        [-72, 101, 101, -74, -75, 101, -71, -73, -95, -96, -89, 101, -90, ]),
    'AND': (
        [67, 116, 122, 124, 144, 169, 170, 171, 172, 174, 175, 176,
         177, 178, 179, 180, ],
        [-72, -71, 142, -85, 142, -95, -96, -97, -89, -90, -82, 142,
         -84, -86, -87, -88, ]), 'OR': (
        [67, 116, 122, 124, 144, 169, 170, 171, 172, 174, 175, 176, 177, 178,
         179,
         180, ],
        [-72, -71, 143, -85, 143, -95, -96, -97, -89, -90, -82, -83, -84, -86,
         -87,
         -88, ]), 'LIMIT': (
        [67, 102, 110, 111, 114, 116, 122, 124, 138, 161, 169, 170, 171, 172,
         174,
         175, 176, 177, 178, 179, 180, ],
        [-72, -77, -74, -75, -104, -71, -76, -85, 164, -73, -95, -96, -97, -89,
         -90,
         -82, -83, -84, -86, -87, -88, ]), ')': (
        [67, 116, 124, 127, 128, 130, 132, 144, 152, 153, 154, 166, 167, 168,
         169,
         170, 171, 172, 174, 175, 176, 177, 178, 179, 180, 182, 190, 191, 193,
         194,
         195, 196, ],
        [-72, -71, -85, 155, -61, 158, 159, 177, -62, -65, -66, 186, -92, -94,
         -95,
         -96, -97, -89, -90, -82, -83, -84, -86, -87, -88, -60, 195, 196, -91,
         -93,
         -63, -64, ]), '(': (
        [78, 79, 82, 101, 117, 123, 142, 143, 152, 153, 154, 157, 192, ],
        [103, 104, 106, 123, 140, 123, 123, 123, 181, -65, -66, 183, 140, ]),
    'PASSWORD': ([80, ], [105, ]), 'ADD': ([83, ], [107, ]),
    'VALUES': ([90, ], [117, ]),
    'PRIMARY': ([103, 107, 156, ], [129, 129, 129, ]),
    'STRING': (
        [105, 140, 141, 145, 146, 147, 148, 149, 150, 151, 164, 187,
         188, ],
        [131, 169, 169, 169, -102, -103, -98, -99, -100, -101, 169,
         169, 169, ]),
    'TO': ([109, 110, 111, 161, ], [135, -74, -75, -73, ]),
    'INT': ([126, ], [153, ]), 'CHAR': ([126, ], [154, ]),
    'KEY': ([129, ], [157, ]), 'NUMBER': (
        [140, 141, 145, 146, 147, 148, 149, 150, 151, 164, 181, 187, 188, ],
        [170, 170, 170, -102, -103, -98, -99, -100, -101, 170, 190, 170,
         170, ]),
    'NULL': (
        [140, 146, 147, 187, 188, ], [171, 171, 171, 171, 171, ]), }

_lr_action = {}
for _k, _v in _lr_action_items.items():
    for _x, _y in zip(_v[0], _v[1]):
        if not _x in _lr_action:  _lr_action[_x] = {}
        _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start': ([0, ], [1, ]), 'command': ([0, ], [2, ]),
                  'ddl': ([0, ], [3, ]), 'dml': ([0, ], [4, ]),
                  'utility': ([0, ], [5, ]), 'nothing': (
        [0, 71, 72, 73, 74, 76, 91, 99, 114, 138, 163, 173, ],
        [6, 95, 95, 95, 95, 102, 102, 95, 102, 165, 95, 102, ]),
                  'createtable': ([0, ], [7, ]), 'createindex': ([0, ], [8, ]),
                  'droptable': ([0, ], [9, ]), 'dropindex': ([0, ], [10, ]),
                  'showtables': ([0, ], [11, ]), 'alerttable': ([0, ], [12, ]),
                  'createuser': ([0, ], [13, ]), 'grantuser': ([0, ], [14, ]),
                  'revokeuser': ([0, ], [15, ]), 'query': ([0, ], [16, ]),
                  'insert': ([0, ], [17, ]), 'delete': ([0, ], [18, ]),
                  'update': ([0, ], [19, ]), 'train': ([0, ], [20, ]),
                  'register': ([0, ], [21, ]), 'load': ([0, ], [22, ]),
                  'save': ([0, ], [23, ]), 'connect': ([0, ], [24, ]),
                  'set': ([0, ], [25, ]), 'exit': ([0, ], [26, ]),
                  'print': ([0, ], [27, ]),
                  'power_list': ([32, 33, ], [54, 62, ]),
                  'power_type': ([32, 33, 85, ], [55, 55, 112, ]),
                  'non_mselect_clause': (
                      [34, 38, 39, 40, 41, ], [63, 71, 72, 73, 74, ]),
                  'non_mrelattr_list': (
                      [34, 38, 39, 40, 41, 88, ], [64, 64, 64, 64, 64, 115, ]),
                  'relattr': (
                      [34, 38, 39, 40, 41, 88, 92, 101, 123, 141, 142, 143,
                       145, ],
                      [66, 66, 66, 66, 66, 66, 119, 125, 125, 172, 125, 125,
                       172, ]), 'opas_clause': (
        [71, 72, 73, 74, 99, 163, ], [93, 96, 97, 98, 121, 184, ]),
                  'opwhere_clause': (
                      [76, 91, 114, 173, ], [100, 118, 138, 189, ]),
                  'non_mrelation_list': ([84, 86, 87, 108, 135, 136, 137, ],
                                         [109, 113, 114, 134, 160, 161, 162, ]),
                  'relation': ([84, 86, 87, 108, 135, 136, 137, ],
                               [110, 110, 110, 110, 110, 110, 110, ]),
                  'non_mcond_list': (
                      [101, 123, 142, 143, ], [122, 144, 175, 176, ]),
                  'condition': ([101, 123, 142, 143, ], [124, 124, 124, 124, ]),
                  'non_mattrtype_list': ([103, 156, ], [127, 182, ]),
                  'attrtype': ([103, 107, 156, ], [128, 133, 128, ]),
                  'inservalue_list': ([117, 192, ], [139, 197, ]),
                  'op': ([125, ], [145, ]), 'type': ([126, ], [152, ]),
                  'oplimit_clause': ([138, ], [163, ]),
                  'non_mvalue_list': ([140, 187, 188, ], [166, 193, 194, ]),
                  'value': ([140, 141, 145, 164, 187, 188, ],
                            [167, 174, 174, 185, 167, 167, ]), 'null_value': (
        [140, 146, 147, 187, 188, ], [168, 179, 180, 168, 168, ]),
                  'relattr_or_value': ([141, 145, ], [173, 178, ]), }

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
    for _x, _y in zip(_v[0], _v[1]):
        if not _x in _lr_goto: _lr_goto[_x] = {}
        _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
    ("S' -> start", "S'", 1, None, None, None),
    ('start -> command', 'start', 1, 'p_start', 'parser.py', 18),
    ('start -> command ;', 'start', 2, 'p_start', 'parser.py', 19),
    ('command -> ddl', 'command', 1, 'p_command', 'parser.py', 23),
    ('command -> dml', 'command', 1, 'p_command', 'parser.py', 24),
    ('command -> utility', 'command', 1, 'p_command', 'parser.py', 25),
    ('command -> nothing', 'command', 1, 'p_command', 'parser.py', 26),
    ('ddl -> createtable', 'ddl', 1, 'p_ddl', 'parser.py', 31),
    ('ddl -> createindex', 'ddl', 1, 'p_ddl', 'parser.py', 32),
    ('ddl -> droptable', 'ddl', 1, 'p_ddl', 'parser.py', 33),
    ('ddl -> dropindex', 'ddl', 1, 'p_ddl', 'parser.py', 34),
    ('ddl -> showtables', 'ddl', 1, 'p_ddl', 'parser.py', 35),
    ('ddl -> alerttable', 'ddl', 1, 'p_ddl', 'parser.py', 36),
    ('ddl -> createuser', 'ddl', 1, 'p_ddl', 'parser.py', 37),
    ('ddl -> grantuser', 'ddl', 1, 'p_ddl', 'parser.py', 38),
    ('ddl -> revokeuser', 'ddl', 1, 'p_ddl', 'parser.py', 39),
    ('dml -> query', 'dml', 1, 'p_dml', 'parser.py', 44),
    ('dml -> insert', 'dml', 1, 'p_dml', 'parser.py', 45),
    ('dml -> delete', 'dml', 1, 'p_dml', 'parser.py', 46),
    ('dml -> update', 'dml', 1, 'p_dml', 'parser.py', 47),
    ('dml -> train', 'dml', 1, 'p_dml', 'parser.py', 48),
    ('dml -> register', 'dml', 1, 'p_dml', 'parser.py', 49),
    ('dml -> load', 'dml', 1, 'p_dml', 'parser.py', 50),
    ('dml -> save', 'dml', 1, 'p_dml', 'parser.py', 51),
    ('dml -> connect', 'dml', 1, 'p_dml', 'parser.py', 52),
    ('dml -> set', 'dml', 1, 'p_dml', 'parser.py', 53),
    ('utility -> exit', 'utility', 1, 'p_utility', 'parser.py', 58),
    ('utility -> print', 'utility', 1, 'p_utility', 'parser.py', 59),
    ('showtables -> SHOW TABLES', 'showtables', 2, 'p_showtables', 'parser.py',
     64),
    ('createuser -> CREATE USER ID PASSWORD STRING', 'createuser', 5,
     'p_createuser', 'parser.py', 69),
    (
        'grantuser -> GRANT power_list ON non_mrelation_list TO non_mrelation_list',
        'grantuser', 6, 'p_grantuser', 'parser.py', 74),
    (
        'revokeuser -> REVOKE power_list ON non_mrelation_list FROM non_mrelation_list',
        'revokeuser', 6, 'p_revokeuser', 'parser.py', 79),
    ('power_list -> power_list , power_type', 'power_list', 3, 'p_power_list',
     'parser.py', 84),
    ('power_list -> power_type', 'power_list', 1, 'p_power_list', 'parser.py',
     85),
    ('power_type -> SELECT', 'power_type', 1, 'p_power_type', 'parser.py', 93),
    ('power_type -> UPDATE', 'power_type', 1, 'p_power_type', 'parser.py', 94),
    ('power_type -> INSERT', 'power_type', 1, 'p_power_type', 'parser.py', 95),
    ('power_type -> DELETE', 'power_type', 1, 'p_power_type', 'parser.py', 96),
    ('power_type -> PRINT', 'power_type', 1, 'p_power_type', 'parser.py', 97),
    ('power_type -> ALL', 'power_type', 1, 'p_power_type', 'parser.py', 98),
    ('alerttable -> ALERT TABLE ID ADD attrtype', 'alerttable', 5,
     'p_alerttable', 'parser.py', 104),
    ('alerttable -> ALERT TABLE ID DROP non_mrelation_list', 'alerttable', 5,
     'p_alerttable', 'parser.py', 105),
    ('createtable -> CREATE TABLE ID ( non_mattrtype_list )', 'createtable', 6,
     'p_createtable', 'parser.py', 113),
    ('createindex -> CREATE INDEX ID ( ID )', 'createindex', 6, 'p_createindex',
     'parser.py', 118),
    ('droptable -> DROP TABLE ID', 'droptable', 3, 'p_droptable', 'parser.py',
     123),
    ('dropindex -> DROP INDEX ID ( ID )', 'dropindex', 6, 'p_dropindex',
     'parser.py', 128),
    ('print -> PRINT ID', 'print', 2, 'p_print', 'parser.py', 133),
    ('exit -> EXIT', 'exit', 1, 'p_exit', 'parser.py', 138),
    (
        'query -> SELECT non_mselect_clause FROM non_mrelation_list opwhere_clause oplimit_clause opas_clause',
        'query', 7, 'p_query', 'parser.py', 143),
    ('insert -> INSERT INTO ID VALUES inservalue_list', 'insert', 5, 'p_insert',
     'parser.py', 148),
    ('inservalue_list -> ( non_mvalue_list ) , inservalue_list',
     'inservalue_list', 5, 'p_inservalue_list', 'parser.py', 153),
    ('inservalue_list -> ( non_mvalue_list )', 'inservalue_list', 3,
     'p_inservalue_list', 'parser.py', 154),
    ('delete -> DELETE FROM ID opwhere_clause', 'delete', 4, 'p_delete',
     'parser.py', 162),
    ('update -> UPDATE ID SET relattr EQ relattr_or_value opwhere_clause',
     'update', 7, 'p_update', 'parser.py', 167),
    ('train -> TRAIN non_mselect_clause opas_clause', 'train', 3, 'p_train',
     'parser.py', 172),
    ('register -> REGISTER non_mselect_clause opas_clause', 'register', 3,
     'p_register', 'parser.py', 177),
    ('load -> LOAD non_mselect_clause opas_clause', 'load', 3, 'p_load',
     'parser.py', 182),
    ('save -> SAVE OVERWRITE TABLE opas_clause', 'save', 4, 'p_save',
     'parser.py', 187),
    ('connect -> CONNECT JDBC opwhere_clause', 'connect', 3, 'p_connect',
     'parser.py', 192),
    (
        'set -> SET non_mselect_clause opas_clause', 'set', 3, 'p_set',
        'parser.py',
        197),
    (
        'non_mattrtype_list -> attrtype , non_mattrtype_list',
        'non_mattrtype_list',
        3, 'p_non_mattrtype_list', 'parser.py', 202),
    ('non_mattrtype_list -> attrtype', 'non_mattrtype_list', 1,
     'p_non_mattrtype_list', 'parser.py', 203),
    ('attrtype -> ID type', 'attrtype', 2, 'p_attrtype', 'parser.py', 211),
    ('attrtype -> ID type ( NUMBER )', 'attrtype', 5, 'p_attrtype', 'parser.py',
     212),
    ('attrtype -> PRIMARY KEY ( ID )', 'attrtype', 5, 'p_attrtype', 'parser.py',
     213),
    ('type -> INT', 'type', 1, 'p_type', 'parser.py', 223),
    ('type -> CHAR', 'type', 1, 'p_type', 'parser.py', 224),
    ('non_mselect_clause -> non_mrelattr_list', 'non_mselect_clause', 1,
     'p_non_mselect_clause', 'parser.py', 229),
    ('non_mselect_clause -> *', 'non_mselect_clause', 1, 'p_non_mselect_clause',
     'parser.py', 230),
    ('non_mrelattr_list -> relattr , non_mrelattr_list', 'non_mrelattr_list', 3,
     'p_non_mrelattr_list', 'parser.py', 235),
    ('non_mrelattr_list -> relattr', 'non_mrelattr_list', 1,
     'p_non_mrelattr_list', 'parser.py', 236),
    ('relattr -> ID . ID', 'relattr', 3, 'p_relattr', 'parser.py', 244),
    ('relattr -> ID', 'relattr', 1, 'p_relattr', 'parser.py', 245),
    (
        'non_mrelation_list -> relation , non_mrelation_list',
        'non_mrelation_list',
        3, 'p_non_mrelation_list', 'parser.py', 253),
    ('non_mrelation_list -> relation', 'non_mrelation_list', 1,
     'p_non_mrelation_list', 'parser.py', 254),
    ('relation -> ID', 'relation', 1, 'p_relation', 'parser.py', 262),
    ('opwhere_clause -> WHERE non_mcond_list', 'opwhere_clause', 2,
     'p_opwhere_clause', 'parser.py', 267),
    ('opwhere_clause -> nothing', 'opwhere_clause', 1, 'p_opwhere_clause',
     'parser.py', 268),
    ('oplimit_clause -> LIMIT value', 'oplimit_clause', 2, 'p_oplimit_clause',
     'parser.py', 274),
    ('oplimit_clause -> nothing', 'oplimit_clause', 1, 'p_oplimit_clause',
     'parser.py', 275),
    ('opas_clause -> AS ID', 'opas_clause', 2, 'p_opas_clause', 'parser.py',
     281),
    ('opas_clause -> nothing', 'opas_clause', 1, 'p_opas_clause', 'parser.py',
     282),
    ('non_mcond_list -> non_mcond_list AND non_mcond_list', 'non_mcond_list', 3,
     'p_non_mcond_list', 'parser.py', 288),
    ('non_mcond_list -> non_mcond_list OR non_mcond_list', 'non_mcond_list', 3,
     'p_non_mcond_list', 'parser.py', 289),
    ('non_mcond_list -> ( non_mcond_list )', 'non_mcond_list', 3,
     'p_non_mcond_list', 'parser.py', 290),
    ('non_mcond_list -> condition', 'non_mcond_list', 1, 'p_non_mcond_list',
     'parser.py', 291),
    ('condition -> relattr op relattr_or_value', 'condition', 3, 'p_condition',
     'parser.py', 301),
    ('condition -> relattr EQ null_value', 'condition', 3, 'p_condition',
     'parser.py', 302),
    ('condition -> relattr NE null_value', 'condition', 3, 'p_condition',
     'parser.py', 303),
    ('relattr_or_value -> relattr', 'relattr_or_value', 1, 'p_relattr_or_value',
     'parser.py', 308),
    ('relattr_or_value -> value', 'relattr_or_value', 1, 'p_relattr_or_value',
     'parser.py', 309),
    ('non_mvalue_list -> value , non_mvalue_list', 'non_mvalue_list', 3,
     'p_non_mvalue_list', 'parser.py', 314),
    ('non_mvalue_list -> value', 'non_mvalue_list', 1, 'p_non_mvalue_list',
     'parser.py', 315),
    ('non_mvalue_list -> null_value , non_mvalue_list', 'non_mvalue_list', 3,
     'p_non_mvalue_list', 'parser.py', 316),
    ('non_mvalue_list -> null_value', 'non_mvalue_list', 1, 'p_non_mvalue_list',
     'parser.py', 317),
    ('value -> STRING', 'value', 1, 'p_value_string', 'parser.py', 325),
    ('value -> NUMBER', 'value', 1, 'p_value_number', 'parser.py', 330),
    ('null_value -> NULL', 'null_value', 1, 'p_null_value', 'parser.py', 335),
    ('op -> LT', 'op', 1, 'p_op', 'parser.py', 340),
    ('op -> LE', 'op', 1, 'p_op', 'parser.py', 341),
    ('op -> GT', 'op', 1, 'p_op', 'parser.py', 342),
    ('op -> GE', 'op', 1, 'p_op', 'parser.py', 343),
    ('op -> EQ', 'op', 1, 'p_op', 'parser.py', 344),
    ('op -> NE', 'op', 1, 'p_op', 'parser.py', 345),
    ('nothing -> <empty>', 'nothing', 0, 'p_nothing', 'parser.py', 350),
]
