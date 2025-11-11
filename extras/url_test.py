import requests

urls = [
    # Technology
    "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1488590528505-98d2b385aade?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1484788984921-700e0e30337a?w=1200&h=800&fit=crop",

    # AI/ML
    "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1535378620166-273708d44e4c?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1507146153580-69a1fe6d8aa1?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=1200&h=800&fit=crop",

    # Data Science
    "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1543286386-713bdd548da4?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1509228627152-72ae4624454b?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1527474305487-b87b222841cc?w=1200&h=800&fit=crop",

    # Web Development
    "https://images.unsplash.com/photo-1633356122544-f134324a6cee?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1579468118864-1b9ea3c0db4a?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1487058792252-ba3c8e8e8c3e?w=1200&h=800&fit=crop",

    # Cloud Computing
    "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1667372393119-3d4c48d07fc9?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1639322537228-f710d846310a?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1573164713988-8665fc963095?w=1200&h=800&fit=crop",

    # Cybersecurity
    "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1563986768494-4dee2763ff3f?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1614064641938-3bbee52942c7?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=1200&h=800&fit=crop",

    # Blockchain
    "https://images.unsplash.com/photo-1639762681485-074b7f938ba0?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1621416894569-0f39ed31d247?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1622630998477-20aa696ecb05?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1518546305927-5a555bb7020d?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1605792657660-596af9009e82?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1639322537228-f710d846310a?w=1200&h=800&fit=crop",

    # IoT
    "https://images.unsplash.com/photo-1558346490-a72e53ae2d4f?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1573164713988-8665fc963095?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1581092160562-40aa08e78837?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1558346490-a72e53ae2d4f?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1573164713988-8665fc963095?w=1200&h=800&fit=crop",

    # DevOps
    "https://images.unsplash.com/photo-1667372393119-3d4c48d07fc9?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1639322537228-f710d846310a?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1581092160562-40aa08e78837?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1667372393119-3d4c48d07fc9?w=1200&h=800&fit=crop",

    # Mobile Development
    "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1551650975-87deedd944c3?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1607252650355-f7fd0460ccdb?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1551650975-87deedd944c3?w=1200&h=800&fit=crop",
    "https://images.unsplash.com/photo-1607252650355-f7fd0460ccdb?w=1200&h=800&fit=crop",
]

for url in urls:
    try:
        response = requests.head(url, allow_redirects=True)
        if response.status_code == 404:
            print(f"404 Not Found: {url}")
        else:
            print(f"OK: {url} (Status: {response.status_code})")
    except Exception as e:
        print(f"Error checking {url}: {e}")
