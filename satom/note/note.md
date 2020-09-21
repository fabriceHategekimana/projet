
Structures des tableaux

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
