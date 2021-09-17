import re

pattern=re.compile(r'^[1-9]\d{4}\s(C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)$')

for i in range(int(input(""))):
    print("VALID" if pattern.match(input("")) else "INVALID")
            


