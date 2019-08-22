```
  █████╗ ███████╗ ██████╗██╗██╗    ████████╗███████╗██╗  ██╗████████╗ 
 ██╔══██╗██╔════╝██╔════╝██║██║    ╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝ 
 ███████║███████╗██║     ██║██║       ██║   █████╗   ╚███╔╝    ██║    
 ██╔══██║╚════██║██║     ██║██║       ██║   ██╔══╝   ██╔██╗    ██║    
 ██║  ██║███████║╚██████╗██║██║       ██║   ███████╗██╔╝ ██╗   ██║    
 ╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝╚═╝       ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝    
 ████████╗ ██████╗      █████╗ ██████╗ ████████╗                      
 ╚══██╔══╝██╔═══██╗    ██╔══██╗██╔══██╗╚══██╔══╝                      
    ██║   ██║   ██║    ███████║██████╔╝   ██║                         
    ██║   ██║   ██║    ██╔══██║██╔══██╗   ██║                         
    ██║   ╚██████╔╝    ██║  ██║██║  ██║   ██║                         
    ╚═╝    ╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝                           
  ```
![Python Version](https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

# Summary
* [Introduction](#introduction)<br>
* [To Include and Use](#Include)<br>
* [Characters Supported With Default Font](#SupportedChacareters)<br>

# <a name="introduction"></a>Introduction<br>
  This program has been developed with the purpose of converting texts in ASCII to something beautiful to see.
</br>

# <a name="Include"></a>To Include and Use<br>
```python3
import ASCIITextToArt
	
art = ASCIITextToArt.ASCIITextToArt()
art.printText('Text Here', style='[optional] Color Here')
artList = art.getList('Text Here', style='[optional] Color Here')
artMatrix = art.getMatrix('Text Here', style='[optional] Color Here')
artText = art.getText('Text Here', style='[optional] Color Here')
```


# <a name="SupportedChacareters"></a>Characters Supported With Default Font</br>

```
  █████╗     ██████╗      ██████╗    ██████╗     ███████╗    ███████╗     ██████╗     ██╗  ██╗    ██╗    
 ██╔══██╗    ██╔══██╗    ██╔════╝    ██╔══██╗    ██╔════╝    ██╔════╝    ██╔════╝     ██║  ██║    ██║    
 ███████║    ██████╔╝    ██║         ██║  ██║    █████╗      █████╗      ██║  ███╗    ███████║    ██║    
 ██╔══██║    ██╔══██╗    ██║         ██║  ██║    ██╔══╝      ██╔══╝      ██║   ██║    ██╔══██║    ██║    
 ██║  ██║    ██████╔╝    ╚██████╗    ██████╔╝    ███████╗    ██║         ╚██████╔╝    ██║  ██║    ██║    
 ╚═╝  ╚═╝    ╚═════╝      ╚═════╝    ╚═════╝     ╚══════╝    ╚═╝          ╚═════╝     ╚═╝  ╚═╝    ╚═╝    

      ██╗    ██╗  ██╗    ██╗         ███╗   ███╗    ███╗   ██╗     ██████╗     ██████╗      ██████╗     ██████╗     
      ██║    ██║ ██╔╝    ██║         ████╗ ████║    ████╗  ██║    ██╔═══██╗    ██╔══██╗    ██╔═══██╗    ██╔══██╗    
      ██║    █████╔╝     ██║         ██╔████╔██║    ██╔██╗ ██║    ██║   ██║    ██████╔╝    ██║   ██║    ██████╔╝    
 ██   ██║    ██╔═██╗     ██║         ██║╚██╔╝██║    ██║╚██╗██║    ██║   ██║    ██╔═══╝     ██║▄▄ ██║    ██╔══██╗    
 ╚█████╔╝    ██║  ██╗    ███████╗    ██║ ╚═╝ ██║    ██║ ╚████║    ╚██████╔╝    ██║         ╚██████╔╝    ██║  ██║    
  ╚════╝     ╚═╝  ╚═╝    ╚══════╝    ╚═╝     ╚═╝    ╚═╝  ╚═══╝     ╚═════╝     ╚═╝          ╚══▀▀═╝     ╚═╝  ╚═╝    

 ███████╗    ████████╗    ██╗   ██╗    ██╗   ██╗    ██╗    ██╗    ██╗  ██╗    ██╗   ██╗    ███████╗    
 ██╔════╝    ╚══██╔══╝    ██║   ██║    ██║   ██║    ██║    ██║    ╚██╗██╔╝    ╚██╗ ██╔╝    ╚══███╔╝    
 ███████╗       ██║       ██║   ██║    ██║   ██║    ██║ █╗ ██║     ╚███╔╝      ╚████╔╝       ███╔╝     
 ╚════██║       ██║       ██║   ██║    ╚██╗ ██╔╝    ██║███╗██║     ██╔██╗       ╚██╔╝       ███╔╝      
 ███████║       ██║       ╚██████╔╝     ╚████╔╝     ╚███╔███╔╝    ██╔╝ ██╗       ██║       ███████╗    
 ╚══════╝       ╚═╝        ╚═════╝       ╚═══╝       ╚══╝╚══╝     ╚═╝  ╚═╝       ╚═╝       ╚══════╝    

  ██╗    ██████╗     ██████╗     ██╗  ██╗    ███████╗     ██████╗     ███████╗     █████╗      █████╗      ██████╗     
 ███║    ╚════██╗    ╚════██╗    ██║  ██║    ██╔════╝    ██╔════╝     ╚════██║    ██╔══██╗    ██╔══██╗    ██╔═████╗    
 ╚██║     █████╔╝     █████╔╝    ███████║    ███████╗    ███████╗         ██╔╝    ╚█████╔╝    ╚██████║    ██║██╔██║    
  ██║    ██╔═══╝      ╚═══██╗    ╚════██║    ╚════██║    ██╔═══██╗       ██╔╝     ██╔══██╗     ╚═══██║    ████╔╝██║    
  ██║    ███████╗    ██████╔╝         ██║    ███████║    ╚██████╔╝       ██║      ╚█████╔╝     █████╔╝    ╚██████╔╝    
  ╚═╝    ╚══════╝    ╚═════╝          ╚═╝    ╚══════╝     ╚═════╝        ╚═╝       ╚════╝      ╚════╝      ╚═════╝     

  ██████╗      ██╗ ██╗     ▄▄███▄▄·    ██╗ ██╗       ██╗                  ██╗    ██╗                                                ██████╗     
 ██╔═══██╗    ████████╗    ██╔════╝    ╚═╝██╔╝       ██║       ▄ ██╗▄    ██╔╝    ╚██╗                                        ██╗    ╚════██╗    
 ██║██╗██║    ╚██╔═██╔╝    ███████╗      ██╔╝     ████████╗     ████╗    ██║      ██║    █████╗                              ╚═╝      ▄███╔╝    
 ██║██║██║    ████████╗    ╚════██║     ██╔╝      ██╔═██╔═╝    ▀╚██╔▀    ██║      ██║    ╚════╝                              ██╗      ▀▀══╝     
 ╚█║████╔╝    ╚██╔═██╔╝    ███████║    ██╔╝██╗    ██████║        ╚═╝     ╚██╗    ██╔╝              ███████╗    ██╗    ▄█╗    ╚═╝      ██╗       
  ╚╝╚═══╝      ╚═╝ ╚═╝     ╚═▀▀▀══╝    ╚═╝ ╚═╝    ╚═════╝                 ╚═╝    ╚═╝               ╚══════╝    ╚═╝    ╚═╝             ╚═╝ 

```

