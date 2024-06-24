java
@ExtendWith(SpringExtension.class)
@DataJpaTest
public class UtilityBillServiceTest {

    @Autowired
    private UtilityBillService utilityBillService;

    @Autowired
    private UtilityBillRepository utilityBillRepository;

    @Test
    public void testGetAllUtilityBills() {
        // Create some utility bills
        List<UtilityBill> utilityBills = List.of(
                new UtilityBill("Electricity", "2023-03-01", new Amount(100.00)),
                new UtilityBill("Gas", "2023-04-01", new Amount(50.00)),
                new UtilityBill("Water", "2023-05-01", new Amount(25.00))
        );
        utilityBillRepository.saveAll(utilityBills);

        // Test the getAllUtilityBills() method
        List<UtilityBill> actualUtilityBills = utilityBillService.getAllUtilityBills();

        // Assert that the actual utility bills match the expected utility bills
        assertEquals(utilityBills, actualUtilityBills);
    }

    @Test
    public void testGetUtilityBillById() {
        // Create a utility bill
        UtilityBill utilityBill = new UtilityBill("Electricity", "2023-03-01", new Amount(100.00));
        utilityBillRepository.save(utilityBill);

        // Test the getUtilityBillById() method
        UtilityBill actualUtilityBill = utilityBillService.getUtilityBillById(utilityBill.getId());

        // Assert that the actual utility bill matches the expected utility bill
        assertEquals(utilityBill, actualUtilityBill);
    }
}