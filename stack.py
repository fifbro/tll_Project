class stack(object):
    """implement of stack by tll.  
          data: 2022-08-14 Sunday 12:31:41 CST  
    """

    def __init__(self): #init stack is null,push elem into empty stack
        self._stack_list=[]  #stack_list is private variability
        self._len=0      #len is private variability
        

    def push(self, elem):
        self._stack_list.append(elem)
        self._len=self._len+1

    def pop(self):
        if self.is_empty():
            raise("stack is null")
        else:
            self._stack_list.pop()
            self._len=self._len-1

    def get_top(self):
        top_elem=self._stack_list[-1]
        return top_elem

    def size(self):
        return self._len

    def is_empty(self):
        return  self._len==0

    def clear(self):
        self._stack_list.clear()
        self._len=0


if __name__ == "__main__":
    st = stack()
    array = ""
    while True:
        array = input("input:")
        if( array == "exit"):
            break
        st.push(array)

    print(st.get_top())
    st.pop()
    print(st.get_top())
    st.pop()
    print(st.get_top())
    st.pop()
    # print("st.size()={}".format(st.size()))
    # print("st.get_top()={}".format(st.get_top()))
    # print("st.is_empty()={}".format(st.is_empty()))
    # st.pop()    
    # st.clear()    
