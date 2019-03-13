# .delete(key) => deletes and returns a value associated with the key
# e.g.  ruby h = {:first_name => "Coding", :last_name => "Dojo"} h.delete(:last_name) print h # => {:first_name => "Coding"}
# .empty? => returns true if hash contains no key-value pairs
# .has_key?(key) => true or false
# .has_value?(value) => true or false

h = {food: "chicken wings", sport: "basketball", car: "civic", shoe: "air max", show: "the wire", book: "none"}

h.delete(:book)
h.empty?
h.has_key?(:food)
h.has_key?(:key)
h.has_value?("basketball")
h.has_value?("football")