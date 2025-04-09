# Roman Numeral Converter <i>2025</i>
<img style= "width:100px" src="https://png.pngtree.com/png-vector/20220610/ourmid/pngtree-mascot-icon-illustration-of-bust-of-an-ancient-roman-emperor-png-image_4971369.png">
  
The Roman Numeral Converter is a simple Python application that converts Roman numerals into their respective integer values. It supports additive and subtractive numeral patterns (such as IV, IX, XL, etc.) and offers basic input validation to ensure accuracy.

<h2>Features</h2> 
<li><b>Roman Numeral to Integer Conversion:</b> Converts Roman numeral strings to their equivalent integer values.</li>
<li><b>Subtractive Notation Support:</b> Correctly handles patterns such as 'IV', 'IX', 'XL', 'XC', 'CD', and 'CM'.</li>
<li><b>Live Interaction:</b> Users can repeatedly convert numerals until they choose to quit.</li>
<li><b>Input Validation:</b> Ensures input contains only valid Roman numeral characters (I, V, X, L, C, D or M).</li>


<h2>Installation</h2> 
<ol>
<li>Clone the repository:</li>

    git clone https://github.com/MarianaAa01/Convert-Roman-Numerals.git

<li>Navigate to the project directory:</li>
   
    cd Convert-Roman-Numerals

</ol>


<h2>Usage</h2> 
<ol> 
  
<li><b>Run the application:</b></li>
   
    python3 romanConverter.py


<li><b>Follow the prompts:</b></li>
<ul>
<li>Enter a Roman numeral string (e.g., <code>XIV</code>, <code>MCMLXXX</code>).</li> 
<li>See the corresponding integer output.</li>
<li>Type <code>Q</code> to exit the program.</li>
</ul>
</ol>

<h2>Code Structure</h2>
<ol> 
<li><b>Input Handling:</b> 
The <code>get_user_input</code> function asks the user for a Roman numeral string or quit command.</li>
<li><b>Validation:</b> The <code>is_valid_roman</code> function checks that all characters in the input are valid Roman numerals.</li>
<li><b>Conversion Logic:</b> The <code>roman_to_int</code> function performs the actual conversion, handling both basic and subtractive notation.</li>
<li><b>Main Loop:</b> Continuously prompts the user until they enter <code>Q</code> to quit.</li>
</ol>

<h4>Example</h4>

```bash
Enter the roman numerals you want to convert (Q to quit): XLII
The roman numerals you entered translate to: 42.

Enter the roman numerals you want to convert (Q to quit): Q
Exiting the program.

