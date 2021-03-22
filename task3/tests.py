from PageObject import GoogleCloud
from Locators import Locators

def test_calculation(browser):
    # 1. Открыть https://cloud.google.com/
    page = GoogleCloud(browser,"https://cloud.google.com/")
    page.open()

    # 2. Нажав кнопку поиска по порталу вверху страницы, ввести в поле поиска"Google Cloud Platform Pricing Calculator"
    # 3. Запустить поиск, нажав кнопку поиска.
    page.search("Google Cloud Platform Pricing Calculator")

    # 4. В результатах поиска кликнуть "Google Cloud Platform Pricing Calculator" и перейти на страницу калькулятора.
    page.choose_result_by_link_text("Google Cloud Platform Pricing Calculator")

    # 5. Активировать раздел COMPUTE ENGINE вверху страницы
    page.switch_to_frame_by_locator(Locators.DEFAULT_FRAME)
    page.switch_to_frame_by_locator(Locators.DEFAULT_FRAME)
    page.choose_section_by_title('Compute Engine')

    # 6. Заполнить форму следующими данными:
    # Number of instances: 4
    page.enter_number_instances(4) 
    # What are these instances for?: оставить пустым
    # Operating System / Software: Free: Debian, CentOS, CoreOS, Ubuntu, or other User Provided OS
    # VM Class: Regular
    # Instance type: n1-standard-8    (vCPUs: 8, RAM: 30 GB)
    page.select('Series', 'n1')
    page.select('Instance type', 'CP-COMPUTEENGINE-VMIMAGE-N1-STANDARD-8')
    
    # Выбрать Add GPUs
    page.add_gpu()
    page.select('Number of GPUs', 1)

    # Number of GPUs: 1
    # GPU type: NVIDIA Tesla V100
    page.select('GPU type', 'NVIDIA_TESLA_V100')

    # Local SSD: 2x375 Gb
    page.select('Local SSD', 2)

    # Datacenter location: Taiwan (asia-east1)
    page.select('Datacenter location', 'asia-east1')

    # Commited usage: 1 Year
    page.select('Committed usage', 1)

    # 7. Нажать Add to Estimate
    page.submit_instances()

    # 8. Проверить соответствие данных следующих полей: VM Class, Instance type, Region, local SSD, commitment term
    # VM class: regular
    # Instance type: n1-standard-8
    # Region: Taiwan
    # Total available local SSD space 2x375 GiB
    # Commitment term: 1 Year
    estimated_fields = page.get_estimated_fields()

    assert estimated_fields['expected_vm_class'] == 'regular'
    assert estimated_fields['expected_instance_type'] == 'n1-standard-8'
    assert estimated_fields['expected_region'] == "Taiwan"
    assert estimated_fields['expected_local_ssd'] == "2x375"
    assert estimated_fields['expected_commitment_term'] == '1'


    # 9. Проверить что сумма аренды в месяц совпадает с суммой получаемой при ручном прохождении теста.
    assert page.total_cost().split()[4] == '5,523.47'