public class UtilityBillManagement {

    public static void main(String[] args) {
        // Create a list of utility bills
        List<UtilityBill> bills = new ArrayList<>();
        bills.add(new UtilityBill("Electricity", 120.00));
        bills.add(new UtilityBill("Gas", 80.00));
        bills.add(new UtilityBill("Water", 50.00));

        // Create a list of payments
        List<Payment> payments = new ArrayList<>();
        payments.add(new Payment("Electricity", 100.00));
        payments.add(new Payment("Gas", 50.00));

        // Calculate the total amount due
        double totalDue = 0.0;
        for (UtilityBill bill : bills) {
            totalDue += bill.getAmount();
        }
        for (Payment payment : payments) {
            totalDue -= payment.getAmount();
        }

        // Format the total due as a currency string
        NumberFormat currencyFormatter = NumberFormat.getCurrencyInstance();
        String totalDueFormatted = currencyFormatter.format(totalDue);

        // Display the summary of utility bills and payments
        System.out.println("Utility Bill Summary");
        System.out.println("---------------------");
        System.out.println("Total Due: " + totalDueFormatted);
        System.out.println();
        System.out.println("Bills:");
        for (UtilityBill bill : bills) {
            System.out.println(" - " + bill.getType() + ": " + currencyFormatter.format(bill.getAmount()));
        }
        System.out.println();
        System.out.println("Payments:");
        for (Payment payment : payments) {
            System.out.println(" - " + payment.getType() + ": " + currencyFormatter.format(payment.getAmount()));
        }
    }
}