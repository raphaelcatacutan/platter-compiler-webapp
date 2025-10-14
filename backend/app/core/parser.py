# AST Nodes
from app.core.lexer import ASSIGN_OPS


class Program:
    def __init__(self, decls, start):
        self.decls = decls
        self.start = start

    def __repr__(self):
        return f"Program(decls={self.decls}, start={self.start})"
class Declaration:
    def __init__(self, dtype, vars): self.dtype, self.vars = dtype, vars
class Recipe:
    def __init__(self, serve_type, name, spices, body):
        self.serve_type, self.name, self.spices, self.body = serve_type, name, spices, body
class StartRecipe:
    def __init__(self, body): self.body = body
class Statement:
    def __init__(self, kind, value=None): self.kind, self.value = kind, value
class Pack:
    def __init__(self, body):
        self.body = body
class Assignment:
    def __init__(self, target, op, expr):
        # target: ('var', name) or ('index', name, index_expr)
        self.target = target
        self.op = op
        self.expr = expr
    def __repr__(self):
        return f"Assignment(target={self.target}, op={self.op}, expr={self.expr})"
class TablePrototype:
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields
    def __repr__(self):
        return f"TablePrototype({self.name}, fields={self.fields})"
class TableInstance:
    def __init__(self, typename, name, init):
        self.typename = typename
        self.name = name
        self.init = init
    def __repr__(self):
        return f"TableInstance({self.typename}, {self.name}, init={self.init})"
class StartPlatter:
    def __init__(self, params, body):
        self.params = params
        self.body = body

    def __repr__(self):
        return f"StartPlatter(params={self.params}, body={self.body})"



class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current = tokens[0]

    def advance(self):
        self.pos += 1
        self.current = self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def eat(self, type_, value=None):
        if self.current.type == type_ and (value is None or self.current.value == value):
            self.advance()
        else:
            raise Exception(f"Expected {type_} {value}, got {self.current}")

    def peek(self, n=1):
        if self.pos + n < len(self.tokens):
            return self.tokens[self.pos + n]
        return None

    # === Grammar ===
    def parse_program(self):
        decls = []
        # consume until we hit "piece of start"
        while not (
                self.current.type == "KEYWORD"
                and self.current.value == "piece"
                and self.peek().type == "KEYWORD"
                and self.peek().value == "of"
                and self.peek(2).type == "KEYWORD"
                and self.peek(2).value == "start"
        ):
            if self.current.type == "KEYWORD" and self.current.value == "prepare":
                decls.append(self.parse_recipes())
            elif self.current.type == "KEYWORD" and self.current.value == "table":
                decls.extend(self.parse_declarations())
            elif self.current.type == "KEYWORD" and (
                    self.current.value in {"piece", "feast", "crumb", "sip", "flag", "character"}
                    or self.current.value.endswith("[]")
            ):
                decls.extend(self.parse_declarations())
            else:
                self.advance()
        # now we are at "piece of start"
        start = self.parse_start()
        return Program(decls, start)

    def parse_recipes(self):
        recipes = []
        while self.current.type == "KEYWORD" and self.current.value == "prepare":
            self.advance()
            serve_type = self.current.value
            self.advance()
            self.eat("KEYWORD", "of")
            name = self.current.value
            self.eat("IDENTIFIER")
            self.eat("SYMBOL", "(")
            spices = []
            if self.current.type != "KEYWORD" or self.current.value != "none":
                while self.current.type != "SYMBOL" or self.current.value != ")":
                    dtype = self.current.value
                    self.advance()
                    self.eat("KEYWORD", "of")
                    varname = self.current.value
                    self.eat("IDENTIFIER")
                    spices.append((dtype, varname))
                    if self.current.type == "SYMBOL" and self.current.value == ",":
                        self.advance()
                    else:
                        break
            else:
                self.eat("KEYWORD", "none")
            self.eat("SYMBOL", ")")
            body = self.parse_platter()
            recipes.append(Recipe(serve_type, name, spices, body))
        return recipes

    def parse_declarations(self):
        decls = []

        # table prototype
        if self.current.type == "KEYWORD" and self.current.value == "table":
            proto = self.parse_table_prototype()
            decls.append(proto)
            return decls

        # variable / set declarations (piece, pieces[], etc.)
        while self.current.type == "KEYWORD" and (
                self.current.value in {"piece", "feast", "crumb", "sip", "flag", "character"}
                or self.current.value.endswith("[]")
        ):
            dtype = self.current.value
            self.advance()
            self.eat("KEYWORD", "of")
            names = []
            while self.current.type == "IDENTIFIER":
                name = self.current.value
                self.advance()
                init = None
                if self.current.type == "OP" and self.current.value == "=":
                    self.advance()
                    if self.current.type == "SYMBOL" and self.current.value == "[":
                        # array/set literal
                        init = self.parse_array_literal()
                    else:
                        init = self.parse_expression()
                names.append((name, init))
                if self.current.type == "SYMBOL" and self.current.value == ",":
                    self.advance()
                    continue
                break
            self.eat("TERMINATOR", "..")
            decls.append(Declaration(dtype, names))
            # do not loop if only single declaration per line required by grammar — adjust if needed
        # table instance declaration (PrototypeName of id = [...].. or expr)
        if self.current is not None and self.current.type == "IDENTIFIER" and self.peek().type == "KEYWORD" and self.peek().value == "of":
            # Example: Person of p1 = [ age = 20.. name = "John".. ]..
            proto_name = self.current.value
            self.advance()
            self.eat("KEYWORD", "of")
            name = self.current.value
            self.eat("IDENTIFIER")
            self.eat("OP", "=")
            if self.current.type == "SYMBOL" and self.current.value == "[":
                # check if table literal or empty initializer
                if self.peek().type == "IDENTIFIER" and self.peek(1).type == "OP" and self.peek(1).value == "=":
                    init = self.parse_table_literal()
                elif self.peek().type == "SYMBOL" and self.peek(1).type == "SYMBOL" and self.peek(1).value == "]":
                    # empty initializer []
                    self.advance();
                    self.eat("SYMBOL", "]")
                    init = {"table_literal": []}
                else:
                    # treat as table literal by default
                    init = self.parse_table_literal()
            else:
                init = self.parse_expression()
            self.eat("TERMINATOR", "..")
            decls.append(TableInstance(proto_name, name, init))

        return decls

    def parse_array_literal(self):
        items = []
        self.eat("SYMBOL", "[")
        while not (self.current.type == "SYMBOL" and self.current.value == "]"):
            # allow nested arrays: if '[' => nested set
            if self.current.type == "SYMBOL" and self.current.value == "[":
                # look ahead: if next is IDENTIFIER followed by '=' → it's a table literal
                if self.peek().type == "IDENTIFIER" and self.peek(1).type == "OP" and self.peek(1).value == "=":
                    items.append(self.parse_table_literal())
                else:
                    items.append(self.parse_array_literal())
            else:
                items.append(self.parse_expression())
            if self.current.type == "SYMBOL" and self.current.value == ",":
                self.advance()
                continue
            break
        self.eat("SYMBOL", "]")
        return {"array_literal": items}

    def parse_recipes(self):
        recipes = []
        while self.current.type == "KEYWORD" and self.current.value == "prepare":
            self.advance()
            serve_type = self.current.value
            self.advance()
            self.eat("KEYWORD", "of")
            name = self.current.value
            self.eat("IDENTIFIER")
            self.eat("SYMBOL", "(")
            spices = []
            if self.current.type != "KEYWORD" or self.current.value != "none":
                while self.current.type != "SYMBOL" or self.current.value != ")":
                    dtype = self.current.value
                    self.advance()
                    self.eat("KEYWORD", "of")
                    varname = self.current.value
                    self.eat("IDENTIFIER")
                    spices.append((dtype,varname))
                    if self.current.type == "SYMBOL" and self.current.value == ",":
                        self.advance()
                    else:
                        break
            else:
                self.eat("KEYWORD", "none")
            self.eat("SYMBOL", ")")
            body = self.parse_platter()
            recipes.append(Recipe(serve_type, name, spices, body))
        return recipes

    def parse_start(self):
        self.eat("KEYWORD", "piece")
        self.eat("KEYWORD", "of")
        self.eat("KEYWORD", "start")
        self.eat("SYMBOL", "(")
        params = []
        if not (self.current.type == "SYMBOL" and self.current.value == ")"):
            while True:
                params.append(self.parse_param())
                if self.current.type == "SYMBOL" and self.current.value == ",":
                    self.advance()
                    continue
                break
        self.eat("SYMBOL", ")")
        self.eat("SYMBOL", "{")
        body = []
        while not (self.current.type == "SYMBOL" and self.current.value == "}"):
            stmt = self.parse_statement()
            if isinstance(stmt, list):
                body.extend(stmt)
            else:
                body.append(stmt)
        self.eat("SYMBOL", "}")
        # return StartPlatter(params, body)
        return Recipe("piece", "start", params, body)

    def parse_platter(self):
        self.eat("SYMBOL", "{")
        statements = []
        while not (self.current.type == "SYMBOL" and self.current.value == "}"):
            statements.append(self.parse_statement())
        self.eat("SYMBOL", "}")
        return statements

    def parse_statement(self):
        # local declarations allowed at start of a platter
        if self.current.type == "KEYWORD" and (
                self.current.value in {"piece", "feast", "crumb", "sip", "flag", "character"}
                or self.current.value.endswith("[]")
        ):
            decls = self.parse_declarations()
            # parse_declarations returns a list of Declaration/Prototype/Instance objects
            # return them wrapped as a 'local_decl' Statement for consistency
            return Statement("local_decl", decls)

        # bill(...)..
        if self.current.type == "KEYWORD" and self.current.value == "bill":
            self.advance()
            self.eat("SYMBOL", "(")
            expr = self.parse_expression()
            self.eat("SYMBOL", ")")
            self.eat("TERMINATOR", "..")
            return Statement("bill", expr)

        # serve ... ..
        if self.current.type == "KEYWORD" and self.current.value == "serve":
            self.advance()
            expr = self.parse_expression()
            self.eat("TERMINATOR", "..")
            return Statement("serve", expr)

        # identifier-based statements: assignment, index/field assignment, call, var_read
        if self.current.type == "IDENTIFIER":
            name = self.current.value
            self.advance()

            # --- array or table access: starts with '[' after identifier ---
            if self.current is not None and self.current.type == "SYMBOL" and self.current.value == "[":
                # consume '['
                self.advance()

                # table field access if inside brackets is IDENTIFIER then ']'
                if self.current is not None and self.current.type == "IDENTIFIER" and self.peek().type == "SYMBOL" and self.peek().value == "]":
                    field = self.current.value
                    self.advance()
                    self.eat("SYMBOL", "]")
                    # expect assignment operator for write: p1[field] = expr..
                    if self.current is not None and self.current.type == "OP" and self.current.value in ASSIGN_OPS:
                        op = self.current.value
                        self.advance()
                        expr = self.parse_expression()
                        self.eat("TERMINATOR", "..")
                        return Statement("assign", Assignment(("field", name, field), op, expr))
                    # if it's a read: p1[field].. (bare read)
                    if self.current is not None and self.current.type == "TERMINATOR" and self.current.value == "..":
                        self.advance()
                        return Statement("table_field_read", ("table_field", name, field))
                    raise Exception(f"Expected assignment or terminator after table field access, got {self.current}")

                # otherwise it's array/set indexing: index is an expression
                idx_expr = self.parse_expression()
                self.eat("SYMBOL", "]")
                # array assignment: r[idx] = expr..
                if self.current is not None and self.current.type == "OP" and self.current.value in ASSIGN_OPS:
                    op = self.current.value
                    self.advance()
                    expr = self.parse_expression()
                    self.eat("TERMINATOR", "..")
                    return Statement("assign", Assignment(("index", name, idx_expr), op, expr))
                # array read: r[idx]..
                if self.current is not None and self.current.type == "TERMINATOR" and self.current.value == "..":
                    self.advance()
                    return Statement("index_read", ("index_read", name, idx_expr))
                raise Exception(f"Expected assignment or terminator after index access, got {self.current}")

            # --- plain assignment: x = expr.. ---
            if self.current is not None and self.current.type == "OP" and self.current.value in ASSIGN_OPS:
                op = self.current.value
                self.advance()
                expr = self.parse_expression()
                self.eat("TERMINATOR", "..")
                return Statement("assign", Assignment(("var", name), op, expr))

            # --- function/recipe call: name(args).. ---
            if self.current is not None and self.current.type == "SYMBOL" and self.current.value == "(":
                self.advance()
                args = []
                if not (self.current.type == "SYMBOL" and self.current.value == ")"):
                    while True:
                        args.append(self.parse_expression())
                        if self.current.type == "SYMBOL" and self.current.value == ",":
                            self.advance()
                            continue
                        break
                self.eat("SYMBOL", ")")
                self.eat("TERMINATOR", "..")
                return Statement("call", (name, args))

            # bare variable read: x..
            if self.current is not None and self.current.type == "TERMINATOR" and self.current.value == "..":
                self.advance()
                return Statement("var_read", name)

            raise Exception(f"Unknown statement start after identifier: {self.current}")

        # nothing matched
        raise Exception(f"Unknown statement start: {self.current}")

    # Expressions (simplified)
    def parse_expression(self):
        tok = self.current

        # simple literals
        if tok.type in {"NUMBER", "STRING", "CHAR"}:
            self.advance()
            # return a small tuple describing the literal
            if tok.type == "NUMBER":
                return ("number", tok.value)
            if tok.type == "STRING":
                return ("string", tok.value)
            return ("char", tok.value)

        # boolean flag keywords
        if tok.type == "KEYWORD" and tok.value in {"up", "down"}:
            self.advance()
            return ("flag", tok.value)

        # identifier: variable, function call, array access, or table field access
        if tok.type == "IDENTIFIER":
            name = tok.value
            self.advance()

            # --- array or table access: name[ ... ] ---
            if self.current is not None and self.current.type == "SYMBOL" and self.current.value == "[":
                # consume '['
                self.advance()

                # if the thing inside brackets is a bare IDENTIFIER followed immediately by ']'
                # treat as table field access: p1[age]
                if self.current is not None and self.current.type == "IDENTIFIER" and self.peek().type == "SYMBOL" and self.peek().value == "]":
                    field = self.current.value
                    self.advance()
                    self.eat("SYMBOL", "]")
                    return ("table_field", name, field)

                # otherwise parse an expression as index (array access / computed index)
                idx_expr = self.parse_expression()
                self.eat("SYMBOL", "]")
                return ("array_access", name, idx_expr)

            # --- function/recipe call in expression: name(args) ---
            if self.current is not None and self.current.type == "SYMBOL" and self.current.value == "(":
                self.advance()
                args = []
                if not (self.current.type == "SYMBOL" and self.current.value == ")"):
                    while True:
                        args.append(self.parse_expression())
                        if self.current.type == "SYMBOL" and self.current.value == ",":
                            self.advance()
                            continue
                        break
                self.eat("SYMBOL", ")")
                return ("call", name, args)

            # plain variable reference
            return ("var", name)

        # array literal or table literal as expression
        if tok.type == "SYMBOL" and tok.value == "[":
            # need to decide whether this is a set literal ([1,2,3]) or a table literal ([field = value.. ...])
            # peek: if after '[' we see IDENTIFIER then OP '=' later before '..' pairs -> table_literal
            # simple heuristic: peek next two tokens; if IDENTIFIER then OP '=' treat as table literal
            if self.peek().type == "IDENTIFIER" and self.peek(1).type == "OP" and self.peek(1).value == "=":
                return self.parse_table_literal()
            return self.parse_array_literal()

        # table literal using braces { ... } if your grammar uses {} for table (some docs show [])
        # if your table literal uses '[' (we handled above), this is optional. Keep for safety:
        if tok.type == "SYMBOL" and tok.value == "{":
            return self.parse_table_literal()

        raise Exception(f"Unexpected expression token: {tok}")

    def parse_table_prototype(self):
        self.eat("KEYWORD", "table")
        self.eat("KEYWORD", "of")
        name = self.current.value
        self.eat("IDENTIFIER")

        self.eat("OP", "=")
        self.eat("SYMBOL", "[")

        fields = []
        while not (self.current.type == "SYMBOL" and self.current.value == "]"):
            field_decls = self.parse_declarations()
            fields.extend(field_decls)

        self.eat("SYMBOL", "]")
        self.eat("TERMINATOR", "..")
        return TablePrototype(name, fields)

    def parse_table_instance(self, typename):
        self.eat("KEYWORD", "of")
        name = self.current.value
        self.eat("IDENTIFIER")

        self.eat("OP", "=")

        if self.current.type == "SYMBOL" and self.current.value == "[":
            init = self.parse_table_literal()
        elif self.current.type == "SYMBOL" and self.current.value == "]":
            init = []  # empty initializer
        else:
            raise Exception(f"Invalid table initializer at {self.current}")

        self.eat("TERMINATOR", "..")
        return TableInstance(typename, name, init)

    def parse_table_literal(self):
        # table literal form in your spec uses brackets with 'field = value..' pairs
        self.eat("SYMBOL", "[")
        fields = []
        while not (self.current.type == "SYMBOL" and self.current.value == "]"):
            if self.current.type != "IDENTIFIER":
                raise Exception(f"Expected field name in table literal, got {self.current}")
            field_name = self.current.value
            self.advance()
            self.eat("OP", "=")
            value = self.parse_expression()
            self.eat("TERMINATOR", "..")
            fields.append((field_name, value))
        self.eat("SYMBOL", "]")
        return {"table_literal": fields}

