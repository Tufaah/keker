from keker import *
# In this example we will take a look at all Scraping (classes/methods)


html_test = '''
value="https://mail.keker.com/"><input type="hidden" name="fretpath" value=""><input type="hidden" name="clean" value=""><input type="hidden" name="service" value=""><input type="hidden" name="origin" value=""><input type="hidden" name="policy" value=""><input type="hidden" name="is_pdd" value=""><input type="hidden" name="csrf_token" value="69f0f15df43a936460f669ebe498761f2527501c:1656196806076"><div class="AuthLoginInputToggle-wrapper"><div class="AuthLoginInputToggle-type"><button data-t="button:default" data-type="login" type="button" class="Button2 Button2_size_l Button2_view_default" autocomplete="off"><span class="Button2-Text">Mail</span></button></div><div class="AuthLoginInputToggle-type"><button data-t="button:clear" data-type="phone" type="button" class="Button2 Button2_size_l Button2_view_clear"
<h2 style="background-color:DodgerBlue;">Hello World</h2>
<script>
    let query = '457102503';
    let id = '5612';
    let ran = "abc1"
    var ran = "abc2";
    const ran = "abc3"
    let _username = 'tufaah';
</script>
<h1>JsScraper - Test made by: @tufaah</h1>
<script>let f = 'faff';</script>
<script>let f = 'faff';</script> <script>let f = 'xxx';</script>
</html>
'''
# Let's say that we have this html code


# > (javaScript) Class Methods
# To get a value from the javaScript code

print(Scrap.javaScript.javaScript(html_test))
# Return the whole JavaScript code as a list

print(Scrap.javaScript.search("let query = '<>'", html_test))
# Search for a value in the JavaScript code
# It will get the value between the <>

print(Scrap.javaScript.find('ran = "<>"', html_test))
# Find all values in the JavaScript code
# It will get the value between the <>
print("\n")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# > (value) Class Methods
# To get a value from the html code!
# Such as csrf token and etc..

print(Scrap.value.search('name="csrf_token" value="<>"', html_test))
# Search for a value in the html code
# It will get the value between the <>

#print(Scrap.javaScript.search('value', "html_code"))
# Find all values in the html code
# It will get the value between the <>

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #