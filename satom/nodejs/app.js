const neo4j = require('neo4j-driver')

const auth= "Jenny";
const password= "Jenny";
const uri="localhost:7474/browser/";

const driver = neo4j.driver(uri, neo4j.auth.basic(auth, password))
const session = driver.session()
const personName = 'Alice'

async function myFunction(){
	try {
		  const result = await session.run(
			      'CREATE (a:Person {name: $name}) RETURN a',
			      { name: personName }
			    )

		  const singleRecord = result.records[0]
		  const node = singleRecord.get(0)

		  console.log(node.properties.name)
	} finally {
		  await session.close()
	}
	// on application exit:
	 await driver.close()
}
