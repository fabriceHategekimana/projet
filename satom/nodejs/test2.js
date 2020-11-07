const neo4j = require('neo4j-driver')
var uri = "neo4j://localhost:7687";
var user = "neo4j";
var password = "neo4j";

const driver = neo4j.driver(uri, neo4j.auth.basic(user, password))
//const session = driver.session()
//var session = driver.session({  defaultAccessMode: neo4j.session.READ })
var session = driver.session({ 
  database: 'neo4j',
    defaultAccessMode: neo4j.session.WRITE
    })

// It is possible to execute read transactions that will benefit from automatic
// retries on both single instance ('bolt' URI scheme) and Causal Cluster
// ('neo4j' URI scheme) and will get automatic load balancing in cluster deployments
var readTxResultPromise = session.readTransaction(txc => {
  // used transaction will be committed automatically, no need for explicit commit/rollback

  var result = txc.run('MATCH (person:Person) RETURN person LIMIT 1')
  // at this point it is possible to either return the result or process it and return the
  // result of processing it is also possible to run more statements in the same transaction
  return result
})

// returned Promise can be later consumed like this:
readTxResultPromise
  .then(result => {
    console.log(result.records[0]._fields[0].properties);
    session.close();
  })
  .catch(error => {
    console.log(error)
  })
  .then(() => {
	session.close();
	driver.close();
  });

