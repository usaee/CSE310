import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int deposit;
        int withdraw;
        int balance = 1000;
            try (Scanner s = new Scanner(System.in)) {
                while(true){
                    System.out.println("\nWelcome To Java ATM Services");
                    System.out.println("1. Withdraw Funds");
                    System.out.println("2. Deposit Funds");
                    System.out.println("3. Check Balance");
                    System.out.println("4. Exit");
                    System.out.print("Please select an option: ");

                    int choice = s.nextInt();

                    switch (choice) {
                        case 1:
                        System.out.print("Enter withdraw amount: ");
                        withdraw = s.nextInt();
                        if(balance >= withdraw){
                            balance = balance - withdraw;
                            System.out.println("\nFunds are being dispensed");
                        }
                        else {
                            System.out.println("\nInsufficient Balance");
                        }
                        System.out.println("");
                    break;
                
                case 2:
                        System.out.print("Enter deposit amount: ");
                        deposit = s.nextInt();
                        balance = balance + deposit;
                        System.out.println("\nFunds deposited successfully");
                        System.out.println("");
                        break;
                
                case 3:
                        System.out.println("\nBalance: " + balance);
                        System.err.println("");
                        break;
                
                case 4:
                        System.out.println("\nGoodbye.\n");
                        System.exit(0);
                }
      }
            }
    }
}
