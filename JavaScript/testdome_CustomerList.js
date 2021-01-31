// Implement the showCustomers function so that it renders customers as list items. The first argument to the function, customers, is an array of objects with the name and email properties. The second argument to the function, targetList, is an unordered HTML list to which each customer should be added as a separate list item.

// The name and email properties should be added as two paragraphs inside the list item. At first, the email paragraph element should not be present in the DOM. The email paragraph element should be added to the DOM after the name is clicked, and it should be removed from the DOM when the name is clicked again.

// For example, the following code:

// document.body.innerHTML = `
// <div>
//   <ul id="customers">
//   </ul>
// </div>
// `;
// let customers = [{name: "John", email: "john@example.com"},
//                  {name: "Mary", email: "mary@example.com"}];
// showCustomers(customers, document.getElementById("customers"));

// let customerParagraph = document.querySelectorAll("li > p")[0];
// if(customerParagraph) {
//   customerParagraph.click();
// }
// console.log(document.body.innerHTML);
// Should render:

// <div>
//   <ul id="customers">
//     <li>
//       <p>John</p>
//       <p>john@example.com</p>
//     </li>
//     <li>
//       <p>Mary</p>
//     </li>
//   </ul>
// </div>

function addDeleteEmail(list, mail)
{
    if (list.children.length == 2)
    {
      list.removeChild(list.lastElementChild);
    }
    else
    {
    let p = document.createElement("p");
    let text = document.createTextNode(mail);
    p.appendChild(text);
    list.appendChild(p);
    }
}

function showCustomers(customers, targetList) 
{
    console.log(customers);
    for (let i = 0; i < customers.length ; i++)
    {
        let para = document.createElement("p");
        let text = document.createTextNode(customers[i].name);
        let list = document.createElement("li")
        para.appendChild(text);
        list.appendChild(para);
        targetList.appendChild(list);
        para.addEventListener("click", function(){
          addDeleteEmail(list, customers[i].email)
        });
    }
    
}
  
  document.body.innerHTML = `
  <div>
    <ul id="customers">
    </ul>
  </div>
  `;
  let customers = [{name: "John", email: "john@example.com"},
                   {name: "Mary", email: "mary@example.com"}];
  console.log(customers[0].name);
  showCustomers(customers, document.getElementById("customers"));
  
  let customerParagraph = document.querySelectorAll("li > p")[0];
  if(customerParagraph) {
    customerParagraph.click();
  }
  console.log(document.body.innerHTML);
