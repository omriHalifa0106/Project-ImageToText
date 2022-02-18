# Project-ImageToText
## מטרת הפרויקט:
הפרויקט  הוא אפליקציית סריקת תמונה לטקסט (OCR) שמאפשרת למשתמש לעלות תמונה עם טקסט באנגלית לאפלקציה, משם התמונה נשלחת אל השרת ובצד השרת ממירה את הטקסט בתמונה לטקסט, ויוצרת בנתיב שנבחר על ידי המשתמש תיקייה שכוללת בתוכה:
אם מדובר בזיהוי תו אחד בודד:
קובץ txt  עם סיווג התו.
קובץ  txt שמכיל בתוכו את כל סיווגי התווים האחרונים של המשתמש.
אם מדובר בזיהוי טקסט בתמונה:
קובץ txt עם סיווג הטקסט שנמצא בתמונה.
קובץ txt שמכיל בתוכו את התרגום של הטקסט מאנגלית לעברית.
קובץ pdf שמכיל בתוכו את סיווג הטקסט בתמונה.
קובץ word שמכיל בתוכו את סיווג הטקסט בתמונה.
תמונה שמראה את רקע התמונה.
## סביבת עבודה:
סביבת העבודה שלי בפרויקט הוא בעיקר פייתון.
את כתיבת צד השרת כתבתי בפייתון. 
את כתיבת צד הלקוח כתבתי בreact native בjava script.
את מודל המכונה כתבתי בפייתון.
## הפרויקט לדוגמה:
אם מדובר בסיווג של תו בודד: 
1. לוחצים על הכפתור PICK AN IMAGE FROM CAMERA ROLL ומעלים תמונה של תו. 
2. בוחרים נתיב בו אנו רוצים לשמור את הסיווג של התו. 
3. לוחצים על הכפתור SEND IMAGE  CHARACTER TO SERVER 
לדוגמה: 

![alt text](https://github.com/omriHalifa0106/Project-ImageToText/blob/main/Images/image1.png?raw=true)

שולחים אל השרת.. 

![alt text](https://github.com/omriHalifa0106/Project-ImageToText/blob/main/Images/image2.png?raw=true)


השרת מחזיר קובץ של סיווג התו בנתיב שבחר המשתמש, וקובץ עם סיווגים אחרונים.

![alt text](https://github.com/omriHalifa0106/Project-ImageToText/blob/main/Images/image3.png?raw=true)
 
אם נבצע את אותו התהליך גם לתו נוסף: 
 
 ![alt text](https://github.com/omriHalifa0106/Project-ImageToText/blob/main/Images/image4.png?raw=true)

 ![alt text](https://github.com/omriHalifa0106/Project-ImageToText/blob/main/Images/image5.png?raw=true)



אם מדובר בסיווג של טקסט: 
1 .לוחצים על הכפתור ROLL CAMERA FROM IMAGE AN PICK ומעלים תמונה של טקסט.
2 .בוחרים נתיב בו אנו רוצים לשמור את הסיווג של הטקסט. 
3. לוחצים על הכפתור SEND IMAGE  Text TO SERVER 
לדוגמה: 


![alt text](https://github.com/omriHalifa0106/Project-ImageToText/blob/main/Images/image6.png?raw=true)



שולחים אל השרת...

השרת מחזיר קובץ של סיווג הטקסט בנתיב שבחר המשתמש, ובנוסף מחזיר קבצים : 
1.	קובץ txt עם סיווג הטקסט שנמצא בתמונה. 
2.	קובץ txt שמכיל בתוכו את התרגום של הטקסט מאנגלית לעברית. 
3.	קובץ pdf שמכיל בתוכו את סיווג הטקסט בתמונה.
4.	קובץ word שמכיל בתוכו את סיווג הטקסט בתמונה. 
5.	תמונה שמראה את רקע התמונה. 

![alt text](https://github.com/omriHalifa0106/Project-ImageToText/blob/main/Images/image7.png?raw=true)

תשובות השרת : 

![alt text](https://github.com/omriHalifa0106/Project-ImageToText/blob/main/Images/image8.png?raw=true)

קובץ הטקסט של סיווג התמונה: 

![alt text](https://github.com/omriHalifa0106/Project-ImageToText/blob/main/Images/image9.png?raw=true)

קובץ הטקסט של תרגום התמונה: 

![alt text](https://github.com/omriHalifa0106/Project-ImageToText/blob/main/Images/image10.png?raw=true)

קובץ WORD עם סיווג התמונה:
![alt text](https://github.com/omriHalifa0106/Project-ImageToText/blob/main/Images/image11.png?raw=true)



קובץ Pdf   עם סיווג התמונה: 

![alt text](https://github.com/omriHalifa0106/Project-ImageToText/blob/main/Images/image12.png?raw=true)

