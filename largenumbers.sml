
(*1.1*)
fun intToLgInt(n)= if n<10 then [n] else (n mod 10)::intToLgInt(n div 10);

(*1.2*)
fun LgintToInt([])= raise Empty
  | LgintToInt([elem])= elem 
  | LgintToInt(x::xs)= if length(x::xs)>9 then 1000000000 else x + 10*LgintToInt(xs);

(*1.3*)
fun addLgint([],[])= []
  |addLgint([el],[ele])= if el+ele < 10 then [el+ele] else ((el+ele) mod 10)::[(el+ele) div 10]
  |addLgint(l1,l2)= if length(l1) < length(l2) then addLgint(l1@[0],l2)
else if length(l1) > length(l2) then addLgint(l1,l2@[0]) 
else if hd(l1) + hd(l2)< 10 then (hd(l1)+hd(l2))::addLgint(tl(l1),tl(l2)) 
else ((hd(l1) + hd(l2)) mod 10)::addLgint(1 + hd(tl(l1))::tl(tl(l1)),tl(l2));

(*1.4*)

fun index(n,list)= if n=1 then hd(list) else index(n-1,tl(list));

fun last(list)= index(length(list),list);

fun p(n,i,[])=[]
  |p(n,i,x::xs)= if i=n then xs else x::p(n,i+1,xs);
fun remlast(l)=p(length(l),1,l);

fun LgLesseq([],[])= raise Empty
  |LgLesseq([el],[elm])= if el <= elm then true else false
  |LgLesseq(l1,l2)= if length(l1) > length(l2) then LgLesseq(l1,l2@[0])
else if length(l1) < length(l2) then LgLesseq(l1@[0],l2) 
else if last(l1) < last(l2) then true
else if last(l1) > last(l2) then false 
else LgLesseq(remlast(l1),remlast(l2));
