**Overview** [Nayr's Japanese Core5000](https://ankiweb.net/shared/info/1269450669) Anki deck ([discussion](http://forum.koohii.com/viewtopic.php?id=12704)) contains pronunciations of all five thousand or so sentences in [*A Frequency Dictionary of Japanese* by Yukio Tono, Makoto Yamazaki, and Kikuo Maekawa (2013)](http://www.amazon.com/Frequency-Dictionary-Japanese-Routledge-Dictionaries/dp/0415610133), which contains the top five thousand words in Japanese according to the latest corpus research. I analyzed these sentences to make a histogram table of hiragana occurrences, including dipthongs like きゃ, ちょ, etc. The attached two tables show the results in modern hiragana order, and sorted order.

**Technical notes** I parsed a file containing those sentences (with annotated readings in hiragana, in `core5k-sentences.md`) using the following script and helper file (in `kana.txt`):

```sh
cp core5k-sentences.md sacrifice.md; 
sed '/^$/d' kana.txt | while read i; do 
  echo -n $i " : " ;
  sed -n "s/$i/$i\n/gp" sacrifice.md | grep $i | wc -l;
  sed -ibak "s/$i//g" sacrifice.md; 
done | tee count-kana-core.txt

SUMMED=`cat count-kana-core.txt | awk '{sum+=$3} END {print sum}'`; 
cat count-kana-core.txt | awk -vsum=$SUMMED '{print $1 $2 " " $3 " : " $3/sum*100}' | tee percent-count-kana-core.txt

sort -k2 -t":" -n -r percent-count-kana-core.txt  > sorted-percent-count-kana-core.txt
```
And here's the helper file `kana.txt` containing the kana. Note the dipthongs are listed first, otherwise the simple-minded algorithm above will break.
```
きゃ
きゅ
きょ

しゃ
しゅ
しょ

ちゃ
ちゅ
ちょ

にゃ
にゅ
にょ

ひゃ
ひゅ
ひょ

みゃ
みゅ
みょ

りゃ
りゅ
りょ

ぎゃ
ぎゅ
ぎょ

じゃ
じゅ
じょ

びゃ
びゅ
びょ

ぴゃ
ぴゅ
ぴょ

あ
い
う
え
お

か
き
く
け
こ

さ
し
す
せ
そ


た
ち
つ
て
と

な
に
ぬ
ね
の

は
ひ
ふ
へ
ほ

ま
み
む
め
も

や
ゆ
よ

ら
り
る
れ
ろ

わ
を

ん

が
ぎ
ぐ
げ
ご

ざ
じ
ず
ぜ
ぞ

だ
ぢ
づ
で
ど

ば
び
ぶ
べ
ぼ

ぱ
ぴ
ぷ
ぺ
ぽ
```
This was done to aid in the construction of a Major or Person-Action-Object memory systems