## Crypto analysis for another alphabet (ENG version)
1. Find the **I**:
    - Strategy **I'M**:
      1. A single letter with the `'` and another following single letter, means: **I'm**.
      2. A single letter that's not the **I** found in the point 1, is the letter: **A**.
    - Strategy **I'LL**:
        1. A single letter with the `'` and another two equal letters following, means: **I'll**.
    - Strategy **I'VE**:
        1. A single letter with the `'` and another two different letters following, probably means: **I've**.

2. Find the **E**:
   1. Use the frequency counter and see the most frequent letters.
   2. Use the word counter and check for word by the chars, and see the most frequent 3 char word.
   3. Try to match the last char with the most frequent one, the find the word **THE** and the letter **E**.
   - Try to use the point 3 to make a better decision for finding the word **THE**.

3. Find **N** and **T**:
   - Find words by 3 letters with, after them a `'`, and another letter after: the letter after `'` is the **T**, and the letter before is **N**. (That's because of the words `can't` and `don't`)
   - **BONUS:** if you found the letter **T** by this technique, you can check the point 2, and find for sure the word **THE**.

4. Common two char words (use them to find better solutions): `in, of, to, is, it, on, no, us, at, un, go, an, my, up, me, as, he, we, so, be, by, or, do, if, hi, bi, ex, ok`

5. Common three char words (use them to find better solutions): `the , man, will, are, was, she, her, his, can, has, had, any, all, out, for, the, and, can, you`

6. Exploit "for-sure" information (maybe you know that you should find a "flag" word in a specific place, and you replace the corresponding letters with correct ones).
