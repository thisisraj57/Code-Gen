java
@SpringBootApplication
public class UtilityBillManagementApplication {

    public static void main(String[] args) {
        SpringApplication.run(UtilityBillManagementApplication.class, args);
    }
}

@RestController
@RequestMapping("/utility-bills")
class UtilityBillController {

    @Autowired
    private UtilityBillService utilityBillService;

    @GetMapping
    public List<UtilityBill> getAllUtilityBills() {
        return utilityBillService.getAllUtilityBills();
    }

    @GetMapping("/{id}")
    public UtilityBill getUtilityBillById(@PathVariable Long id) {
        return utilityBillService.getUtilityBillById(id);
    }
}

@Service
class UtilityBillService {

    @Autowired
    private UtilityBillRepository utilityBillRepository;

    public List<UtilityBill> getAllUtilityBills() {
        return utilityBillRepository.findAll();
    }

    public UtilityBill getUtilityBillById(Long id) {
        return utilityBillRepository.findById(id).orElseThrow(() -> new ResourceNotFoundException("Utility bill not found with id: " + id));
    }
}

@Entity
@Table(name = "utility_bills")
class UtilityBill {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String billType;
    private String dueDate;
    private Amount amount;
}