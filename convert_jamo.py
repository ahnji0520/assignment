#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

_CHO_ = 'ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ'
_JUNG_ = 'ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ'
_JONG_ = 'ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ' # index를 1부터 시작해야 함

# 겹자음 : 'ㄳ', 'ㄵ', 'ㄶ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅄ'
# 겹모음 : 'ㅘ', 'ㅙ', 'ㅚ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅢ'

_JA_ = 'ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ'
_MO_ = 'ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅛㅜㅠㅡㅣ'
_EX_ = 'ㄸㅃㅉ'

_JAMO2ENGKEY_ = {
 'ㄱ': 'r',
 'ㄲ': 'R',
 'ㄴ': 's',
 'ㄷ': 'e',
 'ㄸ': 'E',
 'ㄹ': 'f',
 'ㅁ': 'a',
 'ㅂ': 'q',
 'ㅃ': 'Q',
 'ㅅ': 't',
 'ㅆ': 'T',
 'ㅇ': 'd',
 'ㅈ': 'w',
 'ㅉ': 'W',
 'ㅊ': 'c',
 'ㅋ': 'z',
 'ㅌ': 'x',
 'ㅍ': 'v',
 'ㅎ': 'g',
 'ㅏ': 'k',
 'ㅐ': 'o',
 'ㅑ': 'i',
 'ㅒ': 'O',
 'ㅓ': 'j',
 'ㅔ': 'p',
 'ㅕ': 'u',
 'ㅖ': 'P',
 'ㅗ': 'h',
 'ㅘ': 'hk',
 'ㅙ': 'ho',
 'ㅚ': 'hl',
 'ㅛ': 'y',
 'ㅜ': 'n',
 'ㅝ': 'nj',
 'ㅞ': 'np',
 'ㅟ': 'nl',
 'ㅠ': 'b',
 'ㅡ': 'm',
 'ㅢ': 'ml',
 'ㅣ': 'l',
 'ㄳ': 'rt',
 'ㄵ': 'sw',
 'ㄶ': 'sg',
 'ㄺ': 'fr',
 'ㄻ': 'fa',
 'ㄼ': 'fq',
 'ㄽ': 'ft',
 'ㄾ': 'fx',
 'ㄿ': 'fv',
 'ㅀ': 'fg',
 'ㅄ': 'qt'
}

_ENGKEY2JAMO_ = dict(map(reversed, _JAMO2ENGKEY_.items()))

def checkjj(first, second):

    if first == 'ㄱ' and second == 'ㅅ':
        return 'ㄳ'
    elif first == 'ㄴ' and second == 'ㅈ':
        return 'ㄵ'
    elif first == 'ㄴ' and second == 'ㅎ':
        return 'ㄶ'
    elif first == 'ㄹ' and second == 'ㄱ':
        return 'ㄺ'  
    elif first == 'ㄹ' and second == 'ㅁ':
        return 'ㄻ'
    elif first == 'ㄹ' and second == 'ㅂ':
        return 'ㄼ'
    elif first == 'ㄹ' and second == 'ㅅ':
        return 'ㄽ'
    elif first == 'ㄹ' and second == 'ㅌ':
        return 'ㄾ'
    elif first == 'ㄹ' and second == 'ㅍ':
        return 'ㄿ'
    elif first == 'ㄹ' and second == 'ㅎ':
        return 'ㅀ'
    elif first == 'ㅂ' and second == 'ㅅ':
        return 'ㅄ'

    else:
        return 0 

def checkmm(first, second):

    if first == 'ㅗ' and second == 'ㅏ':
        return 'ㅘ'
    elif first == 'ㅗ' and second == 'ㅐ':
        return 'ㅙ'
    elif first == 'ㅗ' and second == 'ㅣ':
        return 'ㅚ'
    elif first == 'ㅜ' and second == 'ㅓ':
        return 'ㅝ'
    elif first == 'ㅜ' and second == 'ㅔ':
        return 'ㅞ'
    elif first == 'ㅜ' and second == 'ㅣ':
        return 'ㅟ'
    elif first == 'ㅡ' and second == 'ㅣ':
        return 'ㅢ'

    else:
        return 0
      
###############################################################################
def is_hangeul_syllable(ch):
    '''한글 음절인지 검사
    '''
    if not isinstance(ch, str):
        return False
    elif len(ch) > 1:
        ch = ch[0]
    
    return 0xAC00 <= ord(ch) <= 0xD7A3

###############################################################################
def compose(cho, jung, jong):
    '''초성, 중성, 종성을 한글 음절로 조합
    cho : 초성
    jung : 중성
    jong : 종성
    return value: 음절
    '''
    if not (0 <= cho <= 18 and 0 <= jung <= 20 and 0 <= jong <= 27):
        return None
    code = (((cho * 21) + jung) * 28) + jong + 0xAC00

    return chr(code)

###############################################################################
# input: 음절
# return: 초, 중, 종성
def decompose(syll):
    '''한글 음절을 초성, 중성, 종성으로 분해
    syll : 한글 음절
    return value : tuple of integers (초성, 중성, 종성)
    '''
    if not is_hangeul_syllable(syll):
        return (None, None, None)
    
    uindex = ord(syll) - 0xAC00
    
    jong = uindex % 28
    jung = ((uindex - jong) // 28) % 21
    cho = ((uindex - jong) // 28) // 21

    return (cho, jung, jong)

###############################################################################
def str2jamo(str):
    '''문자열을 자모 문자열로 변환
    '''
    jamo = []
    for ch in str:
        if is_hangeul_syllable(ch):
            cho, jung, jong = decompose(ch)
            jamo.append( _CHO_[cho])
            jamo.append( _JUNG_[jung])
            if jong != 0:
                jamo.append( _JONG_[jong-1])
        else:
            jamo.append(ch)
    return ''.join(jamo)

###############################################################################
def jamo2engkey(str):
    '''자모 문자열을 키입력 문자열로 변환
    '''
    engkey = []
    for ch in str:
        if ch in _JAMO2ENGKEY_:
            engkey.append(_JAMO2ENGKEY_[ch])
        else:
            engkey.append(ch)
    return ''.join(engkey)

###############################################################################
def engkey2jamo(str):
    '''키입력 문자열을 자모 문자열로 변환
    '''
    jamo = []
    for ch in str:
        if ch in _ENGKEY2JAMO_:
            jamo.append(_ENGKEY2JAMO_[ch])
        else:
            jamo.append(ch)
    return ''.join(jamo)

###############################################################################
def jamo2syllable(str):
    '''자모 문자열을 음절열로 변환
    '''
    syll = []
    tmp = []

    a = 0 
    b = 0
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0

    for i in range(len(str)):
        if str[i] in _JA_:
            a += 1
        elif str[i] in _MO_:
            b += 1
        else:
            if a == 1 and b == 0:
                syll.append(tmp[0])
            elif a == 2 and b == 0:
                syll.append(checkjj(tmp[0], tmp[1]))
            elif a == 1 and b == 1:
                syll.append(compose(_CHO_.find(tmp[0]), _JUNG_.find(tmp[1]), 0))
            elif a == 2 and b == 1:
                syll.append(compose(_CHO_.find(tmp[0]), _JUNG_.find(tmp[1]), _JONG_.find(tmp[2])+1))
            elif a == 3 and b == 1:
                syll.append(compose(_CHO_.find(tmp[0]), _JUNG_.find(tmp[1]), _JONG_.find(checkjj(tmp[2], tmp[3]))+1))
            elif a == 0 and b == 1:
                syll.append(tmp[0])
            elif a == 1 and b == 2:
                syll.append(compose(_CHO_.find(tmp[0]), _JUNG_.find(checkmm(tmp[1], tmp[2])), 0))
            elif a == 2 and b == 2:
                syll.append(compose(_CHO_.find(tmp[0]), _JUNG_.find(checkmm(tmp[1], tmp[2])), _JONG_.find(tmp[3])+1))
            elif a == 2 and b == 3:
                syll.append(compose(_CHO_.find(tmp[0]), _JUNG_.find(checkmm(tmp[1], tmp[2])), _JONG_.find(checkjj(tmp[3], tmp[4]))+1))
            
            tmp = []
            a = 0
            b = 0
            cnt1 = 0
            cnt2 = 0
            cnt3 = 0

            syll.append(str[i])
            continue
            
        if a == 1 and b == 0:
            tmp.append(str[i])
            if i == len(str)-1:
                syll.append(tmp[0])

        elif a == 2 and b == 0:
            if checkjj(str[i-1], str[i]) == 0:
                syll.append(tmp[0])
                tmp = []
                a -= 1
                tmp.append(str[i])
                if i == len(str)-1:
                    syll.append(tmp[0])
            elif checkjj(str[i-1], str[i]) != 0:
                cnt3 = 1 
                tmp.append(str[i])
                if i == len(str)-1:
                    syll.append(checkjj(tmp[0], tmp[1]))
        
        elif a == 3 and b == 0:
            syll.append(checkjj(tmp[0], tmp[1]))
            tmp = []
            a -= 2
            cnt3 = 0
            tmp.append(str[i])
            if i == len(str)-1:
                syll.append(tmp[0])

        elif a == 2 and b == 1 and cnt3 == 1:
            syll.append(tmp[0])
            del tmp[:1]
            a -= 1
            cnt3 = 0
            tmp.append(str[i])
            if i == len(str)-1:
                syll.append(compose(_CHO_.find(tmp[0]), _JUNG_.find(tmp[1]), 0))

        elif a == 1 and b == 1 and cnt1 == 0:
            tmp.append(str[i])
            if i == len(str)-1:
                syll.append(compose(_CHO_.find(tmp[0]), _JUNG_.find(tmp[1]), 0))

        elif a == 2 and b == 1 and cnt3 == 0:
            if str[i] in _EX_:
                syll.append(compose(_CHO_.find(tmp[0]), _JUNG_.find(tmp[1]), 0))
                tmp = []
                a -= 1
                b -= 1
                tmp.append(str[i])
                if i == len(str)-1:
                    syll.append(tmp[0])
            else:
                tmp.append(str[i])
                if i == len(str)-1:
                    syll.append(compose(_CHO_.find(tmp[0]), _JUNG_.find(tmp[1]), _JONG_.find(tmp[2])+1))
        
        elif a == 3 and b == 1:
            if checkjj(str[i-1], str[i]) == 0:
                syll.append(compose(_CHO_.find(tmp[0]), _JUNG_.find(tmp[1]), _JONG_.find(tmp[2])+1))
                tmp = []
                a -= 2
                b -= 1
                tmp.append(str[i])
                if i == len(str)-1:
                    syll.append(tmp[0])
            elif checkjj(str[i-1], str[i]) != 0:
                tmp.append(str[i])
                if i == len(str)-1:
                    syll.append(compose(_CHO_.find(tmp[0]), _JUNG_.find(tmp[1]), _JONG_.find(checkjj(tmp[2], tmp[3]))+1))

        elif a == 4 and b == 1:
            syll.append(compose(_CHO_.find(tmp[0]), _JUNG_.find(tmp[1]), _JONG_.find(checkjj(tmp[2], tmp[3]))+1))
            tmp = []
            a -= 3
            b -= 1
            tmp.append(str[i])
            if i == len(str)-1:
                syll.append(tmp[0])
        
        elif a == 3 and b == 2 and cnt2 == 0:
            syll.append(compose(_CHO_.find(tmp[0]), _JUNG_.find(tmp[1]), _JONG_.find(tmp[2])+1))
            del tmp[:3]
            a -= 2
            b -= 1 
            tmp.append(str[i])
            if i == len(str)-1:
                syll.append(compose(_CHO_.find(tmp[0]), _JUNG_.find(tmp[1]), 0))
        
        elif a == 2 and b == 2 and cnt2 == 0:
            syll.append(compose(_CHO_.find(tmp[0]), _JUNG_.find(tmp[1]), 0))
            del tmp[:2]
            a -= 1
            b -= 1
            tmp.append(str[i])
            if i == len(str)-1:
                syll.append(compose(_CHO_.find(tmp[0]), _JUNG_.find(tmp[1]), 0))

        elif a == 1 and b == 2:
            cnt2 = 1
            if checkmm(str[i-1], str[i]) == 0:
                syll.append(compose(_CHO_.find(tmp[0]), _JUNG_.find(tmp[1]), 0))
                tmp = []
                a -= 1
                b -= 1
                tmp.append(str[i])
                cnt1 = 1
                cnt2 = 0
                if i == len(str)-1:
                    syll.append(tmp[0])
            elif checkmm(str[i-1], str[i]) != 0:
                tmp.append(str[i])
                if i == len(str)-1:
                    syll.append(compose(_CHO_.find(tmp[0]), _JUNG_.find(checkmm(tmp[1], tmp[2])), 0))

        elif a == 2 and b == 2 and cnt2 == 1:
            if str[i] in _EX_:
                syll.append(compose(_CHO_.find(tmp[0]), _JUNG_.find(checkmm(tmp[1], tmp[2])), 0))
                tmp = []
                a -= 1
                b -= 2
                cnt2 = 0
                tmp.append(str[i])
                if i == len(str)-1:
                    syll.append(tmp[0])
            else:
                tmp.append(str[i])
                if i == len(str)-1:
                    syll.append(compose(_CHO_.find(tmp[0]), _JUNG_.find(checkmm(tmp[1], tmp[2])), _JONG_.find(tmp[3])+1))

        elif a == 3 and b == 2 and cnt2 == 1:
            if checkjj(str[i-1], str[i]) == 0:
                syll.append(compose(_CHO_.find(tmp[0]), _JUNG_.find(checkmm(tmp[1], tmp[2])), _JONG_.find(tmp[3])+1))
                tmp = []
                a -= 2
                b -= 2
                cnt2 = 0
                tmp.append(str[i])
                if i == len(str)-1:
                    syll.append(tmp[0])
            elif checkjj(str[i-1], str[i]) != 0:
                tmp.append(str[i])
                if i == len(str)-1:
                    syll.append(compose(_CHO_.find(tmp[0]), _JUNG_.find(checkmm(tmp[1], tmp[2])), _JONG_.find(checkjj(tmp[3], tmp[4]))+1))

        elif a == 4 and b == 2:
            syll.append(compose(_CHO_.find(tmp[0]), _JUNG_.find(checkmm(tmp[1], tmp[2])), _JONG_.find(checkjj(tmp[3], tmp[4]))+1))
            tmp = []
            a -= 3
            b -= 2
            cnt2 = 0
            tmp.append(str[i])
            if i == len(str)-1:
                syll.append(tmp[0])

        elif a == 3 and b == 3:
            syll.append(compose(_CHO_.find(tmp[0]), _JUNG_.find(checkmm(tmp[1], tmp[2])), _JONG_.find(tmp[3])+1))
            del tmp[:4]
            a -= 2
            b -= 2
            cnt2 = 0
            tmp.append(str[i])
            if i == len(str)-1:
                syll.append(compose(_CHO_.find(tmp[0]), _JUNG_.find(tmp[1]), 0))
        
        elif a == 2 and b == 3:
             syll.append(compose(_CHO_.find(tmp[0]), _JUNG_.find(checkmm(tmp[1], tmp[2])), 0))
             del tmp[:3]
             a -= 1
             b -= 2
             cnt2 = 0 
             tmp.append(str[i])
             if i == len(str)-1:
                syll.append(compose(_CHO_.find(tmp[0]), _JUNG_.find(tmp[1]), 0))

        elif a == 1 and b == 3:
            syll.append(compose(_CHO_.find(tmp[0]), _JUNG_.find(checkmm(tmp[1], tmp[2])), 0))
            tmp = []
            a -= 1
            b -= 2
            tmp.append(str[i])
            cnt2 = 0
            cnt1 = 1 
            if i == len(str)-1:
                syll.append(tmp[0])
        
        elif a == 0 and b == 1: 
            cnt1 = 1
            tmp.append(str[i])
            if i == len(str)-1:
                syll.append(tmp[0])

        elif a == 1 and b == 1 and cnt1 == 1: 
            syll.append(tmp[0])
            tmp = []
            b -= 1
            cnt1 = 0
            tmp.append(str[i])
            if i == len(str)-1:
                syll.append(tmp[0])

        elif a == 0 and b == 2:
            if checkmm(str[i-1], str[i]) == 0:
                syll.append(tmp[0])
                tmp = []
                b -= 1
                tmp.append(str[i])
                if i == len(str)-1:
                    syll.append(tmp[0])
            elif checkmm(str[i-1], str[i]) != 0:
                tmp.append(str[i])
                syll.append(checkmm(tmp[0], tmp[1]))
                tmp = []
                b -= 2
                cnt1 = 0 
    
    syllable = ''.join(syll)

    return syllable

###############################################################################  
if __name__ == "__main__":
    
    i = 0
    line = sys.stdin.readline()

    while line:
        line = line.rstrip()
        i += 1
        print('[%06d:0]\t%s' %(i, line)) # 원문
    
        # 문자열을 자모 문자열로 변환 ('닭고기' -> 'ㄷㅏㄺㄱㅗㄱㅣ')
        jamo_str = str2jamo(line)
        print('[%06d:1]\t%s' %(i, jamo_str)) # 자모 문자열

        # 자모 문자열을 키입력 문자열로 변환 ('ㄷㅏㄺㄱㅗㄱㅣ' -> 'ekfrrhrl')
        key_str = jamo2engkey(jamo_str)
        print('[%06d:2]\t%s' %(i, key_str)) # 키입력 문자열
        
        # 키입력 문자열을 자모 문자열로 변환 ('ekfrrhrl' -> 'ㄷㅏㄹㄱㄱㅗㄱㅣ')
        jamo_str = engkey2jamo(key_str)
        print('[%06d:3]\t%s' %(i, jamo_str)) # 자모 문자열

        # 자모 문자열을 음절열로 변환 ('ㄷㅏㄹㄱㄱㅗㄱㅣ' -> '닭고기')
        syllables = jamo2syllable(jamo_str)
        print('[%06d:4]\t%s' %(i, syllables)) # 음절열

        line = sys.stdin.readline()
