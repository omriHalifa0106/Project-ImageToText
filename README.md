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
 

שולחים אל השרת.. 



השרת מחזיר קובץ של סיווג התו בנתיב שבחר המשתמש, וקובץ עם סיווגים אחרונים.


 
 













אם נבצע את אותו התהליך גם לתו נוסף: 
 
 







