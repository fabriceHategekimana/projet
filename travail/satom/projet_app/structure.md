# ns2:Schema

GradeTypes:
  - GradeType (Id, Name,Description Mandatory)
    - values
      - value 
ItemTypes:
  - EntityTypes
    - EntityType:
      - PropertyTypes:
	- PropertyType:
	  - PossibleValues
  - LinkTypes:
    - LinkType:
      - PropertyTypes:
	- PropertyType:
	  - PossibleValues

## EntityType
- Description
- DisplayName
- Id
- Icon

## PropertyType (Toutes les valeurs sont en string)
- Description 
- DisplayName 
- Id (like "PER1", "PER2", etc.)
- LogicalType (like= "SINGLE_LINE_STRING") 
- Mandatory ("true" or "false")
- Position (index like "0", "1", etc.) 
- SemanticTypeId ""
(- MaximumLengthChars ("250" default))

## LogicalType
- SINGLE_LINE_STRING
- Boolean
- Date
- Multiple line string
- Geospacial

## SemanticTypeId example
 guid4DE7370B-60E5-4EB0-860E-4066D3DFD7B6
 guidBE6A2505-B545-464C-B407-51F9847ECE39
 guid4DE7370B-60E5-4EB0-860E-4066D3DFD7B6
 guidBE6A2505-B545-464C-B407-51F9847ECE39
 guidBE6A2505-B545-464C-B407-51F9847ECE39
 guid62B01C18-2E64-46D5-B2FF-3C69B4F76FEB
 guid62B01C18-2E64-46D5-B2FF-3C69B4F76FEB
 guid3C07BD39-5F65-4fb0-B87F-5B633BCF9B04
 
 
 
 
