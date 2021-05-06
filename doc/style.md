# STYLE

* Variable, member and method names in_snake_case.
	_names should be treated as private.
	__names are reserved.

* Class names in CamelCase
	(But, *sigh* the System object is not a Class; rename to "xxl"?)

* Indent and line breakage:
  * indent at four spaces
  * tab stops at eight spaces
  * no spaces before or between tabs
  * no spaces at end of line
  * binary operators; one space on each side, except:
    * no spaces around "." or ".."
    * no spaces around "[" or closing "]"
  * function calls:
    * no spaces between function and argument paren (including "return")!
    * no space between paren and first argument
    * no space between argument and comma
    * one space after a comma
  * one space between keyword (if/while) and open paren
  * a statement that ends with a block does not take a ";"
  * "{" on the same line as the statement, even when labeled.
  * "}" on a line by itself, at same indent as opening statement
	(unless tokens after the "}" are part of the statement,
	 in which case they should follow the "}",
	and the statement should be terminated with ";")
  * statement labels on a separate line,
	 unindented two spaces from statement indent
  * *NOT* currently consistent line breakage and operators!!
	(but probably should be)
