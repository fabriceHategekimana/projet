## companies
![companies](../images/companies.png)
```
companies : { 
	label: label,
	Geopoint: geopoint
}
```

## investors
![investors](../images/investors.png)

```
investors:{ 
	label: label,
	investortype: investortype
}
```

## investments
![investments](../images/investments.png)

```
investments:{ 
	companies: companies,
	investors: investors,
	funded_date: funded_date,
	raised_amount: raised_amount,
	raised_currency_code: raised_currency_code
}
```

## articles
![articles](../images/articles.png)
```
articles:{ 
	title: title,
	author: author,
	id: id,
	companies: list of 'company/[company_Name]',
	pdate: '2012-06-13',
	source: journal,
	title: title,
	url: url,
}
```

Officer Neo4j ICIJ
![officer](../images/officer.png)

Code qui marche

```
GET siren/articles/_search
{ 
  "query": { 
      "join": { 
            "indices": [
	              "companies"
	    ],
	  "on": [
		  "companies",
		  "id"
	  ],
	  "request": { 
		    "query": { 
			"term": { 
			      "label": "Apple"
			  }
		    }
	    }
	}
}
}
```
GET siren/articles/_search
