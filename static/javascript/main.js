let buttons = document.getElementsByClassName('add-to-cart')
let inv = [
  {
    id: '1',
    name: 'Jeans',
    price: '$19.99',
    description: 'the greatest first item'
  },
  {
    id: '2',
    name: 'Shirt',
    price: '$19.99',
    description: 'the greatest first item'
  },
  {
    id: '3',
    name: 'Hat',
    price: '$19.99',
    description: 'the greatest first item'
  }
]
for (let button of buttons) {
  button.addEventListener('click', addToCart(button))
}

function addToCart(button) {
  console.log(button)
}

