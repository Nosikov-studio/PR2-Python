const express = require('express');
const sqlite3 = require('sqlite3').verbose();

const app= express();
let y;

app.get('/', (req, res, next) =>{
  res.send('it is working!!!')
})



//************************Middleware********************************** */
app.use( (req, res, next) =>{  

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
let x = getRandomInt(1, 5);


// Создание нового экземпляра базы данных
const db = new sqlite3.Database('mydatabase.db', (err) => {
  if (err) {
    console.error(err.message);
  }
  console.log('Подключено к базе данных.');
});

sql='CREATE TABLE IF NOT EXISTS verbs( verb_id INTEGER PRIMARY KEY, verb_en TEXT, verb_ru TEXT )'

db.run(sql, (err) => {
    if (err) {
      console.error(err.message);
    }
    // console.log('Таблица создана.');
  });

  
  db.get('SELECT verb_en FROM verbs WHERE verb_id= ?', [x], (err, row) => {
    if (err) {
      console.error(err.message);
    }
    y=row['verb_en']
    console.log(y);
  });

  next();
})
  //***************************************************** */

  app.get('/p', (req, res, next) =>{
    res.send(y)
  })



  app.listen(5000, ()=>{
    console.log('Its started', new Date())
  })