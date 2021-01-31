function registerHandlers() 
{
    var as = document.getElementsByTagName('a');
    console.log(as);
    for (let i = 0; i < as.length; i++) 
    {
      console.log(as[i].text);
      as[i].onclick = function() 
      {
        alert(i);
        return false;
      }
    }
}

registerHandlers();