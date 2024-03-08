import java.util.*;
class Convey 
{
void BillM(int nrr[],int srr[],double arr[],int brr[],String irr[])
{System.out.flush();
int i=0;String ch;
Scanner sc=new Scanner(System.in);
do{
System.out.println("Enter code ");
i=sc.nextInt();
System.out.println("Enter number of items");
nrr[i]=sc.nextInt();
srr[i]=srr[i]-nrr[i];

System.out.println("Enter discount in percentage");
int d=sc.nextInt();

arr[i]=(brr[i]*nrr[i])-((d/100)*(brr[i]*nrr[i]));

System.out.println("To continue adding items press y");
ch=sc.next();

}while( ch.equalsIgnoreCase("y")==true);
Display(nrr,arr,brr,irr);
}
void Display(int nrr[],double arr[],int brr[],String irr[])//code needed for bill format
{System.out.flush();
double bill = 0.0; double gbill=0.0;
 System.out.println("                                "+"V       V  CCCC  OOOO  N     N");
 System.out.println("                                "+" V     V   C     O  O  N N   N");
 System.out.println("                                "+"  V   V    C     O  O  N  N  N");
 System.out.println("                                "+"   V V     C     O  O  N   N N");
 System.out.println("                                "+"    V      CCCC  OOOO  N     N");
 System.out.println();
 System.out.println();
 System.out.println();
 System.out.println(""+"ITEM"+"         "+"QNT"+"             "+"AMT");
 
 
 if (nrr[0]!=0)
     {System.out.println(irr[0]+"       "+nrr[0]+"             "+brr[0]*nrr[0]);
        
         gbill+=arr[0];
        bill=bill+(brr[0]*nrr[0]);}
        if (nrr[1]!=0)
        {System.out.println(irr[1]+"       "+" "+nrr[1]+"             "+brr[1]*nrr[1]);
           gbill+=arr[1];
        bill=bill+(brr[1]*nrr[1]);}
        if (nrr[2]!=0){System.out.println(irr[2]+"  "+nrr[2]+"             "+brr[2]*nrr[2]);
           gbill+=arr[2];
        bill=bill+(brr[2]*nrr[2]);}
        if (nrr[3]!=0){System.out.println(irr[3]+"     "+nrr[3]+"             "+brr[3]*nrr[3]);
           gbill+=arr[3];
        bill=bill+(brr[3]*nrr[3]);}

        if (nrr[4]!=0){System.out.println(irr[4]+"        "+nrr[4]+"             "+brr[4]*nrr[4]);
           gbill+=arr[4];
        bill=bill+(brr[4]*nrr[4]);}
        if (nrr[5]!=0){System.out.println(irr[5]+"         "+nrr[5]+"             "+brr[5]*nrr[5]);  
            gbill+=arr[5];
        bill=bill+(brr[5]*nrr[5]);}
        if (nrr[6]!=0){System.out.println(irr[6]+"    "+nrr[6]+"             "+brr[6]*nrr[6]);
               gbill+=arr[6];
        bill=bill+(brr[6]*nrr[6]);}
            
        if (nrr[7]!=0){System.out.println(irr[7]+"          "+nrr[7]+"             "+brr[7]*nrr[7]);
           gbill+=arr[7];
        bill=bill+(brr[7]*nrr[7]);}
        if (nrr[8]!=0){System.out.println(irr[8]+"      "+nrr[8]+"             "+brr[8]*nrr[8]);
           gbill+=arr[8];
        bill=bill+(brr[8]*nrr[8]);}
         if (nrr[9]!=0){System.out.println(irr[9]+"     "+nrr[9]+"             "+brr[9]*nrr[9]);
               gbill+=arr[9];
        bill=bill+(brr[9]*nrr[9]);}
        System.out.println("TOTAL=                                   "+bill);
        System.out.println("DISCOUNT=  "+"                               -"+(bill-gbill));
        System.out.println("GROSS TOTAL=                              "    +gbill);
        
 
}

void Check(String irr[],int srr[])
{ System.out.flush();
System.out.println("ITEM"+"           "+"CODE"+"          "+"STOCK");
System.out.println(irr[0]+"         "+"0"+"             "+srr[0]);
System.out.println(irr[1]+"     "+"1"+"             "+srr[1]);
System.out.println(irr[2]+"   "+"2"+"             "+srr[2]);
System.out.println(irr[3]+"      "+"3"+"             "+srr[3]);
System.out.println(irr[4]+"         "+"4"+"             "+srr[4]);
System.out.println(irr[5]+"          "+"5"+"             "+srr[5]);
System.out.println(irr[6]+"     "+"6"+"             "+srr[6]);
System.out.println(irr[7]+"           "+"7"+"             "+srr[7]);
System.out.println(irr[8]+"       "+"8"+"             "+srr[8]);
System.out.println(irr[9]+"      "+"9"+"             "+srr[9]);
//code needed for display
}

void Update(int brr[])
{ System.out.flush();
int i=0;String ch;
Scanner sc =new Scanner(System.in); 
do{
System.out.println("ENTER CODE");
i=sc.nextInt();
System.out.println("Enter the number to be added");
int n=sc.nextInt();
brr[i]=brr[i]+n;
System.out.println("To continue updating press y");
ch=sc.next();
}while(ch.equalsIgnoreCase("y")==true);

//code needed to upload new stock status 
} 




public static void main(String args[])
{ 
Scanner sc= new Scanner (System.in);
int brr[]={30,70,20,65,80,12,55,35,15,5};
double arr[]=new double[10];
int nrr[]=new int[10];
String irr[]={"NOODLES","CHOCOLATE","CHIPS/CRISPS","MILKSHAKE","COFFEE","BREAD","STATIONARY","SODA","ADHESIVE","CARRY BAG"};
int srr[]={60,110,55,90,43,54,89,69,28,200};
Convey obj=new Convey ();
int ch;
do
{System.out.println("ENTER 1 FOR MAKING A BIIL" +"/n"+ "ENTER 2 CHECKING STOCK"+"/n"+"ENTER 3 FOR UPDATING STOCK "+"/n"+"ENTER 4 TO EXIT");
ch=sc.nextInt();
switch(ch)
{
case 1:
obj.BillM(nrr,srr,arr,brr,irr);
break;
case 2:
obj.Check(irr,srr);
break;
case 3:

obj.Update(brr);
break;
case 4:
System.out.println("THANK YOU FOR USING Vcon");
break;
default:
System.out.println("WE DON'T DO THAT HERE");
}
}while(ch!=4);}}





