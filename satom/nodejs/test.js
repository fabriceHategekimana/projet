const neo4j = require('neo4j-driver')
var uri = "neo4j://localhost:7687";
var user = "neo4j";
var password = "neo4j";

const driver = neo4j.driver(uri, neo4j.auth.basic(user, password))
//const session = driver.session()
//var session = driver.session({  defaultAccessMode: neo4j.session.READ })
var session = driver.session({ 
  database: 'system',
    defaultAccessMode: neo4j.session.WRITE
    })

session
  .run('MERGE (m:MOVIE) RETURN m', {
    nameParam: 'James'
  })
  .then(result => {
    result.records.forEach(record => {
      console.log(record.get('name'))
    })
  })
  .catch(error => {
    console.log(error)
  })
  .then(() => session.close())

driver.close

