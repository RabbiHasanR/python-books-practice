from sllist import *

def test_push():
    colors = SingleLinkedList()
    colors.push("Pthalo Blue")
    assert colors.count() == 1
    colors.push("Ultramarine Blue")
    assert colors.count() == 2

def test_pop():
    colors = SingleLinkedList()
    colors.push("Magenta")
    colors.push("Alizarin")
    assert colors.pop() == "Alizarin"
    assert colors.pop() == "Magenta"
    assert colors.pop() == None

# def test_unshift():
#     colors = SingleLinkedList()
#     colors.push("Viridian")
#     colors.push("Sap Green")
#     colors.push("Van Dyke")
#     assert colors.unshift() == "Viridian"
#     assert colors.unshift() == "Sap Green"
#     assert colors.unshift() == "Van Dyke"
#     assert colors.unshift() == None

# def test_shift():
#     colors = SingleLinkedList()
#     colors.shift("Cadmium Orange")
#     assert colors.count() == 1
#     colors.shift("Carbazole Violet")
#     assert colors.count() == 2
#     assert
#     assert
#     assert
#     assert
#     colors.pop() == "Cadmium Orange"
#     colors.count() == 1
#     colors.pop() == "Carbazole Violet"
#     colors.count() == 0

# def test_remove():
#     colors = SingleLinkedList()
#     colors.push("Cobalt")
#     colors.push("Zinc White")
#     colors.push("Nickle Yellow")
#     colors.push("Perinone")
#     assert colors.remove("Cobalt") == 0
#     colors.dump("before perinone")
#     assert colors.remove("Perinone") == 2
#     colors.dump("after perinone")
#     assert colors.remove("Nickle Yellow") == 1
#     assert colors.remove("Zinc White") == 0

# def test_first():
#     colors = SingleLinkedList()
#     colors.push("Cadmium Red Light")
#     assert colors.first() == "Cadmium Red Light"
#     colors.push("Hansa Yellow")
#     assert colors.first() == "Cadmium Red Light"
#     colors.shift("Pthalo Green")
#     assert colors.first() == "Pthalo Green"

# def test_last():
#     colors = SingleLinkedList()
#     colors.push("Cadmium Red Light")
#     assert colors.last() == "Cadmium Red Light"
#     colors.push("Hansa Yellow")
#     assert colors.last() == "Hansa Yellow"
#     colors.shift("Pthalo Green")
#     assert colors.last() == "Hansa Yellow"

# def test_get():
#     colors = SingleLinkedList()
#     colors.push("Vermillion")
#     assert colors.get(0) == "Vermillion"
#     colors.push("Sap Green")
#     assert colors.get(0) == "Vermillion"
#     assert colors.get(1) == "Sap Green"
#     colors.push("Cadmium Yellow Light")
#     assert colors.get(0) == "Vermillion"
#     assert colors.get(1) == "Sap Green"
#     assert colors.get(2) == "Cadmium Yellow Light"
#     assert colors.pop() == "Cadmium Yellow Light"
#     assert colors.get(0) == "Vermillion"
#     assert colors.get(1) == "Sap Green"
#     assert colors.get(2) == None
#     colors.pop()
#     assert colors.get(0) == "Vermillion"
#     colors.pop()
#     assert colors.get(0) == None


test_push()
test_pop()