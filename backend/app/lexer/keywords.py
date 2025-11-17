from app.lexer.token import Token
from app.lexer.protocol import LexerProtocol


class LexerKeywords(LexerProtocol):
    
    # All keywords in the Platter language
    KEYWORDS = [
        "alt", "and", "append", "bill", "chars", "check", "choice", "copy", "cut",
        "fact", "flag", "instead", "matches", "menu", "next", "not", "of", "or",
        "order", "pass", "piece", "pow", "prepare", "rand", "remove", "repeat",
        "reverse", "search", "serve", "sip", "size", "sort", "sqrt", "start",
        "stop", "table", "take", "tochars", "topiece", "tosip", "usual"
    ]

    # --- 'a' ---
    def s1(self):
        print("s1")
        self.advance()
        if self.current == "l": return self.s2()
        if self.current == "n": return self.s5()
        if self.current == "p": return self.s8()
        self.restore()
        return None

    def s2(self):  # al
        print("s2")
        self.advance()
        if self.current == "t": return self.s3()
        self.restore()
        return None

    def s3(self):  # alt (Accepting State 4)
        print("s3")
        self.advance()
        if self._match_delimiter(self.paren_dlm): return self.s4()
        self.restore()
        return None

    def s4(self):
        print("s4")
        return Token("alt", self.get_lexeme(), self.start_line, self.start_col)

    def s5(self):  # an
        print("s5")
        self.advance()
        if self.current == "d": return self.s6()
        self.restore()
        return None

    def s6(self):  # and (Accepting State 7)
        print("s6")
        self.advance()
        if self._match_delimiter(self.paren_dlm): return self.s7()
        self.restore()
        return None

    def s7(self):
        print("s7")
        return Token("and", self.get_lexeme(), self.start_line, self.start_col)

    def s8(self):  # ap
        print("s8")
        self.advance()
        if self.current == "p": return self.s9()
        self.restore()
        return None

    def s9(self):  # app
        print("s9")
        self.advance()
        if self.current == "e": return self.s10()
        self.restore()
        return None

    def s10(self):  # appe
        print("s10")
        self.advance()
        if self.current == "n": return self.s11()
        self.restore()
        return None

    def s11(self):  # appen
        print("s11")
        self.advance()
        if self.current == "d": return self.s12()
        self.restore()
        return None

    def s12(self):  # append (Accepting State 13)
        print("s12")
        self.advance()
        if self._match_delimiter(self.paren_dlm): return self.s13()
        self.restore()
        return None

    def s13(self):
        print("s13")
        return Token("append", self.get_lexeme(), self.start_line, self.start_col)

    # --- 'b' ---
    def s14(self):  # b
        print("s14")
        self.advance()
        if self.current == "i": return self.s15()
        self.restore()
        return None

    def s15(self):  # bi
        print("s15")
        self.advance()
        if self.current == "l": return self.s16()
        self.restore()
        return None

    def s16(self):  # bil
        print("s16")
        self.advance()
        if self.current == "l": return self.s17()
        self.restore()
        return None

    def s17(self):  # bill (Accepting State 18)
        print("s17")
        self.advance()
        if self._match_delimiter(self.paren_dlm): return self.s18()
        self.restore()
        return None

    def s18(self):
        print("s18")
        return Token("bill", self.get_lexeme(), self.start_line, self.start_col)

    # --- 'c' ---
    def s19(self):  # c
        print("s19")
        self.advance()
        if self.current == "h": return self.s20()
        if self.current == "o": return self.s34()
        if self.current == "u": return self.s38()
        self.restore()
        return None

    def s20(self):  # ch
        print("s20")
        self.advance()
        if self.current == "a": return self.s21()
        if self.current == "e": return self.s25()
        if self.current == "o": return self.s29()
        self.restore()
        return None

    def s21(self):  # cha
        print("s21")
        self.advance()
        if self.current == "r": return self.s22()
        self.restore()
        return None

    def s22(self):  # char
        print("s22")
        self.advance()
        if self.current == "s": return self.s23()
        self.restore()
        return None

    def s23(self):  # chars (Accepting State 24)
        print("s23")
        self.advance()
        if self._match_delimiter(self.dtype_dlm): return self.s24()
        self.restore()
        return None

    def s24(self):
        print("s24")
        return Token("chars", self.get_lexeme(), self.start_line, self.start_col)

    def s25(self):  # che
        print("s25")
        self.advance()
        if self.current == "c": return self.s26()
        self.restore()
        return None

    def s26(self):  # chec
        print("s26")
        self.advance()
        if self.current == "k": return self.s27()
        self.restore()
        return None

    def s27(self):  # check (Accepting State 28)
        print("s27")
        self.advance()
        if self._match_delimiter(self.paren_dlm): return self.s28()
        self.restore()
        return None

    def s28(self):
        print("s28")
        return Token("check", self.get_lexeme(), self.start_line, self.start_col)

    def s29(self):  # cho
        print("s29")
        self.advance()
        if self.current == "i": return self.s30()
        if self.current == "p": return self.s34()  # 'copy' starts with 'c-o-p'
        self.restore()
        return None

    def s30(self):  # choi
        print("s30")
        self.advance()
        if self.current == "c": return self.s31()
        self.restore()
        return None

    def s31(self):  # choic
        print("s31")
        self.advance()
        if self.current == "e": return self.s32()
        self.restore()
        return None

    def s32(self):  # choice (Accepting State 33)
        print("s32")
        self.advance()
        if self._match_delimiter(self.whitespace_dlm): return self.s33()
        self.restore()
        return None

    def s33(self):
        print("s33")
        return Token("choice", self.get_lexeme(), self.start_line, self.start_col)

    def s34(self):  # cop
        print("s34")
        self.advance()
        if self.current == "p": return self.s35()
        self.restore()
        return None

    def s35(self):  # copy (Accepting State 37)
        print("s35")
        self.advance()
        if self.current == "y": return self.s36()
        self.restore()
        return None

    def s36(self):  # copy (Accepting State 37)
        print("s36")
        self.advance()
        if self._match_delimiter(self.paren_dlm): return self.s37()
        self.restore()
        return None

    def s37(self):  # copy (Accepting State 37)
        print("s37")
        return Token("copy", self.get_lexeme(), self.start_line, self.start_col)

    def s38(self):  # cu
        print("s38")
        self.advance()
        if self.current == "t": return self.s39()
        self.restore()
        return None

    def s39(self):  # cut (Accepting State 40)
        print("s39")
        self.advance()
        if self._match_delimiter(self.paren_dlm): return self.s40()
        self.restore()
        return None

    def s40(self):
        print("s40")
        return Token("cut", self.get_lexeme(), self.start_line, self.start_col)

    # --- 'd' ---
    def s41(self):  # d
        print("s41")
        self.advance()
        if self.current == "o": return self.s42()
        self.restore()
        return None

    def s42(self):  # do
        print("s42")
        self.advance()
        if self.current == "w": return self.s43()
        self.restore()
        return None

    def s43(self):  # dow
        print("s43")
        self.advance()
        if self.current == "n": return self.s44()
        self.restore()
        return None

    def s44(self):  # down (Accepting State 45)
        print("s44")
        self.advance()
        if self._match_delimiter(self.flag_dlm): return self.s45()
        self.restore()
        return None

    def s45(self):
        print("s45")
        return Token("flag_lit", self.get_lexeme(), self.start_line, self.start_col)

    # --- 'f' ---
    def s46(self):  # f
        print("s46")
        self.advance()
        if self.current == "a": return self.s47()
        if self.current == "l": return self.s51()
        self.restore()
        return None

    def s47(self):  # fa
        print("s47")
        self.advance()
        if self.current == "c": return self.s48()
        self.restore()
        return None

    def s48(self):  # fac
        print("s48")
        self.advance()
        if self.current == "t": return self.s49()
        self.restore()
        return None

    def s49(self):  # fact (Accepting State 50)
        print("s49")
        self.advance()
        if self._match_delimiter(self.paren_dlm): return self.s50()
        self.restore()
        return None

    def s50(self):
        print("s50")
        return Token("fact", self.get_lexeme(), self.start_line, self.start_col)

    def s51(self):  # fl
        print("s51")
        self.advance()
        if self.current == "a": return self.s52()
        self.restore()
        return None

    def s52(self):  # fla
        print("s52")
        self.advance()
        if self.current == "g": return self.s53()
        self.restore()
        return None

    def s53(self):  # flag (Accepting State 54)
        print("s53")
        self.advance()
        if self._match_delimiter(self.dtype_dlm): return self.s54()
        self.restore()
        return None

    def s54(self):
        print("s54")
        return Token("flag", self.get_lexeme(), self.start_line, self.start_col)

    # --- 'i' ---
    def s55(self):  # i
        print("s55")
        self.advance()
        if self.current == "n": return self.s56()
        self.restore()
        return None

    def s56(self):  # in
        print("s56")
        self.advance()
        if self.current == "s": return self.s57()
        self.restore()
        return None

    def s57(self):  # ins
        print("s57")
        self.advance()
        if self.current == "t": return self.s58()
        self.restore()
        return None

    def s58(self):  # inst
        print("s58")
        self.advance()
        if self.current == "e": return self.s59()
        self.restore()
        return None

    def s59(self):  # inste
        print("s59")
        self.advance()
        if self.current == "a": return self.s60()
        self.restore()
        return None

    def s60(self):  # instea
        print("s60")
        self.advance()
        if self.current == "d": return self.s61()
        self.restore()
        return None

    def s61(self):  # instead (Accepting State 62)
        print("s61")
        self.advance()
        if self._match_delimiter(self.curly_dlm): return self.s62()
        self.restore()
        return None

    def s62(self):
        print("s62")
        return Token("instead", self.get_lexeme(), self.start_line, self.start_col)

    # --- 'm' ---
    def s63(self):  # m
        print("s63")
        self.advance()
        if self.current == "a": return self.s64()
        if self.current == "e": return self.s71()
        self.restore()
        return None

    def s64(self):  # ma
        print("s64")
        self.advance()
        if self.current == "t": return self.s65()
        self.restore()
        return None

    def s65(self):  # mat
        print("s65")
        self.advance()
        if self.current == "c": return self.s66()
        self.restore()
        return None

    def s66(self):  # matc
        print("s66")
        self.advance()
        if self.current == "h": return self.s67()
        self.restore()
        return None

    def s67(self):  # match
        print("s67")
        self.advance()
        if self.current == "e": return self.s68()
        self.restore()
        return None

    def s68(self):  # matche
        print("s68")
        self.advance()
        if self.current == "s": return self.s69()
        self.restore()
        return None

    def s69(self):  # matches (Accepting State 70)
        print("s69")
        self.advance()
        if self._match_delimiter(self.paren_dlm): return self.s70()
        self.restore()
        return None

    def s70(self):
        print("s70")
        return Token("matches", self.get_lexeme(), self.start_line, self.start_col)

    def s71(self):  # me
        print("s71")
        self.advance()
        if self.current == "n": return self.s72()
        self.restore()
        return None

    def s72(self):  # men
        print("s72")
        self.advance()
        if self.current == "u": return self.s73()
        self.restore()
        return None

    def s73(self):  # menu (Accepting State 74)
        print("s73")
        self.advance()
        if self._match_delimiter(self.paren_dlm): return self.s74()
        self.restore()
        return None

    def s74(self):
        print("s74")
        return Token("menu", self.get_lexeme(), self.start_line, self.start_col)

    # --- 'n' ---
    def s75(self):  # n
        print("s75")
        self.advance()
        if self.current == "e": return self.s76()
        if self.current == "o": return self.s80()
        self.restore()
        return None

    def s76(self):  # ne
        print("s76")
        self.advance()
        if self.current == "x": return self.s77()
        self.restore()
        return None

    def s77(self):  # nex
        print("s77")
        self.advance()
        if self.current == "t": return self.s78()
        self.restore()
        return None

    def s78(self):  # next (Accepting State 79)
        print("s78")
        self.advance()
        if self._match_delimiter(self.term_dlm): return self.s79()
        self.restore()
        return None

    def s79(self):
        print("s79")
        return Token("next", self.get_lexeme(), self.start_line, self.start_col)

    def s80(self):  # no
        print("s80")
        self.advance()
        if self.current == "t": return self.s81()
        self.restore()
        return None

    def s81(self):  # not (Accepting State 82)
        print("s81")
        self.advance()
        if self._match_delimiter(self.paren_dlm): return self.s82()
        self.restore()
        return None

    def s82(self):
        print("s82")
        return Token("not", self.get_lexeme(), self.start_line, self.start_col)

    # --- 'o' ---
    def s83(self):  # o
        print("s83")
        self.advance()
        if self.current == "f": return self.s84()
        if self.current == "r": return self.s86()
        self.restore()
        return None

    def s84(self):  # of (Accepting State 85)
        print("s84")
        self.advance()
        if self._match_delimiter(self.whitespace_dlm): return self.s85()
        self.restore()
        return None

    def s85(self):
        print("s85")
        return Token("of", self.get_lexeme(), self.start_line, self.start_col)

    def s86(self):  # or (Accepting State 87)
        print("s86")
        self.advance()
        if self.current == "d": return self.s88()
        if self._match_delimiter(self.paren_dlm): return self.s87()
        self.restore()
        return None

    def s87(self):
        print("s87")
        return Token("or", self.get_lexeme(), self.start_line, self.start_col)

    def s88(self):  # ord
        print("s88")
        self.advance()
        if self.current == "e": return self.s89()
        self.restore()
        return None

    def s89(self):  # orde
        print("s89")
        self.advance()
        if self.current == "r": return self.s90()
        self.restore()
        return None

    def s90(self):  # order (Accepting State 91)
        print("s90")
        self.advance()
        if self._match_delimiter(self.paren_dlm): return self.s91()
        self.restore()
        return None

    def s91(self):
        print("s91")
        return Token("order", self.get_lexeme(), self.start_line, self.start_col)

    # --- 'p' ---
    def s92(self):  # p
        print("s92")
        self.advance()
        if self.current == "a": return self.s93()
        if self.current == "i": return self.s97()
        if self.current == "o": return self.s102()
        if self.current == "r": return self.s105()
        self.restore()
        return None

    def s93(self):  # pa
        print("s93")
        self.advance()
        if self.current == "s": return self.s94()
        self.restore()
        return None

    def s94(self):  # pas
        print("s94")
        self.advance()
        if self.current == "s": return self.s95()
        self.restore()
        return None

    def s95(self):  # pass (Accepting State 96)
        print("s95")
        self.advance()
        if self._match_delimiter(self.paren_dlm): return self.s96()
        self.restore()
        return None

    def s96(self):
        print("s96")
        return Token("pass", self.get_lexeme(), self.start_line, self.start_col)

    def s97(self):  # pi
        print("s97")
        self.advance()
        if self.current == "e": return self.s98()
        self.restore()
        return None

    def s98(self):  # pie
        print("s98")
        self.advance()
        if self.current == "c": return self.s99()
        self.restore()
        return None

    def s99(self):  # piec
        print("s99")
        self.advance()
        if self.current == "e": return self.s100()
        self.restore()
        return None

    def s100(self):  # piece (Accepting State 101)
        print("s100")
        self.advance()
        if self._match_delimiter(self.dtype_dlm): return self.s101()
        self.restore()
        return None

    def s101(self):
        print("s101")
        return Token("piece", self.get_lexeme(), self.start_line, self.start_col)

    def s102(self):  # po
        print("s102")
        self.advance()
        if self.current == "w": return self.s103()
        self.restore()
        return None

    def s103(self):  # pow (Accepting State 104)
        print("s103")
        self.advance()
        if self._match_delimiter(self.paren_dlm): return self.s104()
        self.restore()
        return None

    def s104(self):
        print("s104")
        return Token("pow", self.get_lexeme(), self.start_line, self.start_col)

    def s105(self):  # pr
        print("s105")
        self.advance()
        if self.current == "e": return self.s106()
        self.restore()
        return None

    def s106(self):  # pre
        print("s106")
        self.advance()
        if self.current == "p": return self.s107()
        self.restore()
        return None

    def s107(self):  # prep
        print("s107")
        self.advance()
        if self.current == "a": return self.s108()
        self.restore()
        return None

    def s108(self):  # prepa
        print("s108")
        self.advance()
        if self.current == "r": return self.s109()
        self.restore()
        return None

    def s109(self):  # prepar
        print("s109")
        self.advance()
        if self.current == "e": return self.s110()
        self.restore()
        return None

    def s110(self):  # prepare (Accepting State 111)
        print("s110")
        self.advance()
        if self._match_delimiter(self.whitespace_dlm): return self.s111()
        self.restore()
        return None

    def s111(self):
        print("s111")
        return Token("prepare", self.get_lexeme(), self.start_line, self.start_col)

    # --- 'r' ---
    def s112(self):  # r
        print("s112")
        self.advance()
        if self.current == "a": return self.s113()
        if self.current == "e": return self.s117()
        self.restore()
        return None

    def s113(self):  # ra
        print("s113")
        self.advance()
        if self.current == "n": return self.s114()
        self.restore()
        return None

    def s114(self):  # ran
        print("s114")
        self.advance()
        if self.current == "d": return self.s115()
        self.restore()
        return None

    def s115(self):  # rand (Accepting State 116)
        print("s115")
        self.advance()
        if self._match_delimiter(self.paren_dlm): return self.s116()
        self.restore()
        return None

    def s116(self):
        print("s116")
        return Token("rand", self.get_lexeme(), self.start_line, self.start_col)

    def s117(self):  # re
        print("s117")
        self.advance()
        if self.current == "m": return self.s118()
        if self.current == "p": return self.s123()
        if self.current == "v": return self.s128()
        self.restore()
        return None

    def s118(self):  # rem
        print("s118")
        self.advance()
        if self.current == "o": return self.s119()
        self.restore()
        return None

    def s119(self):  # remo
        print("s119")
        self.advance()
        if self.current == "v": return self.s120()
        self.restore()
        return None

    def s120(self):  # remov
        print("s120")
        self.advance()
        if self.current == "e": return self.s121()
        self.restore()
        return None

    def s121(self):  # remove (Accepting State 122)
        print("s121")
        self.advance()
        if self._match_delimiter(self.paren_dlm): return self.s122()
        self.restore()
        return None

    def s122(self):
        print("s122")
        return Token("remove", self.get_lexeme(), self.start_line, self.start_col)

    def s123(self):  # rep
        print("s123")
        self.advance()
        if self.current == "e": return self.s124()
        self.restore()
        return None

    def s124(self):  # repe
        print("s124")
        self.advance()
        if self.current == "a": return self.s125()
        self.restore()
        return None

    def s125(self):  # repea
        print("s125")
        self.advance()
        if self.current == "t": return self.s126()
        self.restore()
        return None

    def s126(self):  # repeat (Accepting State 127)
        print("s126")
        self.advance()
        if self._match_delimiter(self.paren_dlm): return self.s127()
        self.restore()
        return None

    def s127(self):
        print("s127")
        return Token("repeat", self.get_lexeme(), self.start_line, self.start_col)

    def s128(self):  # rev
        print("s128")
        self.advance()
        if self.current == "e": return self.s129()
        self.restore()
        return None

    def s129(self):  # reve
        print("s129")
        self.advance()
        if self.current == "r": return self.s130()
        self.restore()
        return None

    def s130(self):  # rever
        print("s130")
        self.advance()
        if self.current == "s": return self.s131()
        self.restore()
        return None

    def s131(self):  # revers
        print("s131")
        self.advance()
        if self.current == "e": return self.s132()
        self.restore()
        return None

    def s132(self):  # reverse (Accepting State 133)
        print("s132")
        self.advance()
        if self._match_delimiter(self.paren_dlm): return self.s133()
        self.restore()
        return None

    def s133(self):
        print("s133")
        return Token("reverse", self.get_lexeme(), self.start_line, self.start_col)

    # --- 's' ---
    def s134(self):  # s
        print("s134")
        self.advance()
        if self.current == "e": return self.s135()
        if self.current == "i": return self.s145()
        if self.current == "o": return self.s151()
        if self.current == "q": return self.s155()
        if self.current == "t": return self.s159()
        self.restore()
        return None

    def s135(self):  # se
        print("s135")
        self.advance()
        if self.current == "a": return self.s136()
        if self.current == "r": return self.s141()
        self.restore()
        return None

    def s136(self):  # sea
        print("s136")
        self.advance()
        if self.current == "r": return self.s137()
        self.restore()
        return None

    def s137(self):  # sear
        print("s137")
        self.advance()
        if self.current == "c": return self.s138()
        self.restore()
        return None

    def s138(self):  # searc
        print("s138")
        self.advance()
        if self.current == "h": return self.s139()
        self.restore()
        return None

    def s139(self):  # search (Accepting State 140)
        print("s139")
        self.advance()
        if self._match_delimiter(self.paren_dlm): return self.s140()
        self.restore()
        return None

    def s140(self):
        print("s140")
        return Token("search", self.get_lexeme(), self.start_line, self.start_col)

    def s141(self):  # ser
        print("s141")
        self.advance()
        if self.current == "v": return self.s142()
        self.restore()
        return None

    def s142(self):  # serv
        print("s142")
        self.advance()
        if self.current == "e": return self.s143()
        self.restore()
        return None

    def s143(self):  # serve (Accepting State 144)
        print("s143")
        self.advance()
        if self._match_delimiter(self.whitespace_dlm): return self.s144()
        self.restore()
        return None

    def s144(self):
        print("s144")
        return Token("serve", self.get_lexeme(), self.start_line, self.start_col)

    def s145(self):  # si
        print("s145")
        self.advance()
        if self.current == "p": return self.s146()
        if self.current == "z": return self.s148()
        self.restore()
        return None

    def s146(self):  # sip (Accepting State 147)
        print("s146")
        self.advance()
        if self._match_delimiter(self.dtype_dlm): return self.s147()
        self.restore()
        return None

    def s147(self):
        print("s147")
        return Token("sip", self.get_lexeme(), self.start_line, self.start_col)

    def s148(self):  # siz
        print("s148")
        self.advance()
        if self.current == "e": return self.s149()
        self.restore()
        return None

    def s149(self):  # size (Accepting State 150)
        print("s149")
        self.advance()
        if self._match_delimiter(self.paren_dlm): return self.s150()
        self.restore()
        return None

    def s150(self):
        print("s150")
        return Token("size", self.get_lexeme(), self.start_line, self.start_col)

    def s151(self):  # so
        print("s151")
        self.advance()
        if self.current == "r": return self.s152()
        self.restore()
        return None

    def s152(self):  # sor
        print("s152")
        self.advance()
        if self.current == "t": return self.s153()
        self.restore()
        return None

    def s153(self):  # sort (Accepting State 154)
        print("s153")
        self.advance()
        if self._match_delimiter(self.paren_dlm): return self.s154()
        self.restore()
        return None

    def s154(self):
        print("s154")
        return Token("sort", self.get_lexeme(), self.start_line, self.start_col)

    def s155(self):  # sq
        print("s155")
        self.advance()
        if self.current == "r": return self.s156()
        self.restore()
        return None

    def s156(self):  # sqr
        print("s156")
        self.advance()
        if self.current == "t": return self.s157()
        self.restore()
        return None

    def s157(self):  # sqrt (Accepting State 158)
        print("s157")
        self.advance()
        if self._match_delimiter(self.paren_dlm): return self.s158()
        self.restore()
        return None

    def s158(self):
        print("s158")
        return Token("sqrt", self.get_lexeme(), self.start_line, self.start_col)

    def s159(self):  # st
        print("s159")
        self.advance()
        if self.current == "a": return self.s160()
        if self.current == "o": return self.s164()
        self.restore()
        return None

    def s160(self):  # sta
        print("s160")
        self.advance()
        if self.current == "r": return self.s161()
        self.restore()
        return None

    def s161(self):  # star
        print("s161")
        self.advance()
        if self.current == "t": return self.s162()
        self.restore()
        return None

    def s162(self):  # start (Accepting State 163)
        print("s162")
        self.advance()
        if self._match_delimiter(self.paren_dlm): return self.s163()
        self.restore()
        return None

    def s163(self):
        print("s163")
        return Token("start", self.get_lexeme(), self.start_line, self.start_col)

    def s164(self):  # sto
        print("s164")
        self.advance()
        if self.current == "p": return self.s165()
        self.restore()
        return None

    def s165(self):  # stop (Accepting State 166)
        print("s165")
        self.advance()
        if self._match_delimiter(self.term_dlm): return self.s166()
        self.restore()
        return None

    def s166(self):
        print("s166")
        return Token("stop", self.get_lexeme(), self.start_line, self.start_col)

    # --- 't' ---
    def s167(self):  # t
        print("s167")
        self.advance()
        if self.current == "a": return self.s168()
        if self.current == "o": return self.s176()
        self.restore()
        return None

    def s168(self):  # ta
        print("s168")
        self.advance()
        if self.current == "b": return self.s169()
        if self.current == "k": return self.s173()
        self.restore()
        return None

    def s169(self):  # tab
        print("s169")
        self.advance()
        if self.current == "l": return self.s170()
        self.restore()
        return None

    def s170(self):  # tabl
        print("s170")
        self.advance()
        if self.current == "e": return self.s171()
        self.restore()
        return None

    def s171(self):  # table (Accepting State 172)
        print("s171")
        self.advance()
        if self._match_delimiter(self.whitespace_dlm): return self.s172()
        self.restore()
        return None

    def s172(self):
        print("s172")
        return Token("table", self.get_lexeme(), self.start_line, self.start_col)

    def s173(self):  # tak
        print("s173")
        self.advance()
        if self.current == "e": return self.s174()
        self.restore()
        return None

    def s174(self):  # take (Accepting State 175)
        print("s174")
        self.advance()
        if self._match_delimiter(self.paren_dlm): return self.s175()
        self.restore()
        return None

    def s175(self):
        print("s175")
        return Token("take", self.get_lexeme(), self.start_line, self.start_col)

    def s176(self):  # to
        print("s176")
        self.advance()
        if self.current == "c": return self.s177()
        if self.current == "p": return self.s183()
        if self.current == "s": return self.s189()
        self.restore()
        return None

    def s177(self):  # toc
        print("s177")
        self.advance()
        if self.current == "h": return self.s178()
        self.restore()
        return None

    def s178(self):  # toch
        print("s178")
        self.advance()
        if self.current == "a": return self.s179()
        self.restore()
        return None

    def s179(self):  # tocha
        print("s179")
        self.advance()
        if self.current == "r": return self.s180()
        self.restore()
        return None

    def s180(self):  # tochar
        print("s180")
        self.advance()
        if self.current == "s": return self.s181()
        self.restore()
        return None

    def s181(self):  # tochars (Accepting State 182)
        print("s181")
        self.advance()
        if self._match_delimiter(self.paren_dlm): return self.s182()
        self.restore()
        return None

    def s182(self):
        print("s182")
        return Token("tochars", self.get_lexeme(), self.start_line, self.start_col)

    def s183(self):  # top
        print("s183")
        self.advance()
        if self.current == "i": return self.s184()
        self.restore()
        return None

    def s184(self):  # topi
        print("s184")
        self.advance()
        if self.current == "e": return self.s185()
        self.restore()
        return None

    def s185(self):  # topie
        print("s185")
        self.advance()
        if self.current == "c": return self.s186()
        self.restore()
        return None

    def s186(self):  # topiec
        print("s186")
        self.advance()
        if self.current == "e": return self.s187()
        self.restore()
        return None

    def s187(self):  # topiece (Accepting State 188)
        print("s187")
        self.advance()
        if self._match_delimiter(self.paren_dlm): return self.s188()
        self.restore()
        return None

    def s188(self):
        print("s188")
        return Token("topiece", self.get_lexeme(), self.start_line, self.start_col)

    def s189(self):  # tos
        print("s189")
        self.advance()
        if self.current == "i": return self.s190()
        self.restore()
        return None

    def s190(self):  # tosi
        print("s190")
        self.advance()
        if self.current == "p": return self.s191()
        self.restore()
        return None

    def s191(self):  # tosip (Accepting State 192)
        print("s191")
        self.advance()
        if self._match_delimiter(self.paren_dlm): return self.s192()
        self.restore()
        return None

    def s192(self):
        print("s192")
        return Token("tosip", self.get_lexeme(), self.start_line, self.start_col)

    # --- 'u' ---
    def s193(self):  # u
        print("s193")
        self.advance()
        if self.current == "p": return self.s194()
        if self.current == "s": return self.s196()
        self.restore()
        return None

    def s194(self):  # up (Accepting State 195)
        print("s194")
        self.advance()
        if self._match_delimiter(self.flag_dlm): return self.s195()
        self.restore()
        return None

    def s195(self):
        print("s195")
        return Token("flag_lit", self.get_lexeme(), self.start_line, self.start_col)

    def s196(self):  # us
        print("s196")
        self.advance()
        if self.current == "u": return self.s197()
        self.restore()
        return None

    def s197(self):  # usu
        print("s197")
        self.advance()
        if self.current == "a": return self.s198()
        self.restore()
        return None

    def s198(self):  # usua
        print("s198")
        self.advance()
        if self.current == "l": return self.s199()
        self.restore()
        return None

    def s199(self):  # usual (Accepting State 200)
        print("s199")
        self.advance()
        if self._match_delimiter(self.colon_dlm): return self.s200()
        self.restore()
        return None

    def s200(self):
        print("s200")
        return Token("usual", self.get_lexeme(), self.start_line, self.start_col)
