const bodyParser = require("body-parser");
const { exec } = require("child_process");

var query="MATCH (o:Officer) RETURN o LIMIT 10;";
//var texte='{"sourceID": "Panama Papers", "valid_until": "The Panama Papers data is current through 2015", "name": "KIM SOO IN", "country_codes": "KOR", "countries": "South Korea", "node_id": "12000001"}';
//var val= JSON.parse(texte);
//console.log(val);

function marshalPerson(person){
	var res="";
	if(person[0] != "{"){
		res={};
	}	
	else{ 
		res= JSON.parse(person);
	}
	return res;
}

function recherche(){
	exec('cd "C:\\Users\\Satom2021\\AppData\\Roaming\\Neo4j Desktop for ICIJ\\Application\\neo4jDatabases\\database-159676c6-fff2-4053-b793-5e38acecc39c\\current\\bin\" && cypher-shell.bat \"'+query+'\"', (error, stdout, stderr) => {
	    if (error) {
		console.log(`error: ${error.message}`);
		return;
	    }
	    if (stderr) {
		console.log(`stderr: ${stderr}`);
		return;
	    }
	    //console.log(`stdout: ${stdout}`);
	    var str= stdout.replace(/\(:Officer\ /g, "");
	    str= str.replace(/\}\)/g, "}");
	    str= str.replace(/\{/g, '{"');
	    str= str.replace(/\:/g, '":');
	    str= str.replace(/\,\ /g, ', "');
	    str= str.split("\n");
	    str= str.map(marshalPerson) ;
	    console.log(str);
	});
}


recherche();

