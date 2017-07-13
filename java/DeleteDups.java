import java.util.HashSet;
import java.util.LinkedList;


class LinkedListNode
{
	public Object data;
	public LinkedListNode next;
	public LinkedListNode prev;

	public LinkedListNode(Object data) {
		this.data=data;
	}
}


class DeleteDups 
{

	public static void main(String[] args) {

				
			
		System.out.println("Hello World!");

	}
	public void deleteDups(LinkedListNode n){
		HashSet<Integer> set = new HashSet<Integer>();
		LinkedListNode previous = null;

		while(n!=null){
			if(set.contain(n.data)){
				previous.next=n.next;
			} else {
				set.add(n.data);
				previous=n;
			}
			n=n.next;
		}	
	}
}
