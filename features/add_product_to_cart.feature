# language:pt
# file:add_product_to_cart.feature
# -- FILE: steps\add_product_to_cart.py

@Google
Funcionalidade: Adicionar produto ao carrinho de compras @add_product
  Cenario: Realizar adição de produto ao carrinho de compras no portal americanas @add_product
    Dado que eu esteja com a home do portal americanas aberto @add_product
    Quando eu inserir o código do produto no campo de busca @add_product
      E clicar no botão de busca @add_product
    Entao a pesquisa é realizada e o produto corespondente é exibido na lista @add_product
      E selecionar o produto @add_product
    Então a página com as informações para compra do produto é exibida @add_product
      E validar as informações do produto @add_product
      E clicar em comprar @add_product
    Então a página de seleção da garantia e do seguro é exibida @add_product
      E clicar em continuar @add_product
    Então a página do carrinho de compras é exibida com o produto adicionado @add_product
      E validar as informações do produto no carrinho de compras @add_product
