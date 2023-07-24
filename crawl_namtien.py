{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "51076cca",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "from selenium import webdriver\n",
    "from selenium.webdriver.chrome.options import Options\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "from selenium.webdriver.common.by import By\n",
    "from time import sleep"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "36a12ee0",
   "metadata": {},
   "outputs": [],
   "source": [
    "pageProduct = requests.get(\"https://xemaynamtien.com/yamaha-nvx-the-he-ii-2023-abs\")\n",
    "soup = BeautifulSoup(pageProduct.text, 'html.parser')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "cea42007",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'honda-lead-dac-biet'"
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "soup.find_all(class_ = 'product')[3].a['href']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "71689c90",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Yamaha NVX Thế Hệ II 2023 ABS\n"
     ]
    }
   ],
   "source": [
    "title = soup.h1.text\n",
    "print(title)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "1d177180",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "55,000,000đ\n",
      "\n"
     ]
    }
   ],
   "source": [
    "price = soup.find(class_=\"price-detail\").text\n",
    "print(price)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "27b76398",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Lượt xem: 2103'"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "soup.find_all(class_ = 'col-md-6')[-1].find_all('p')[-1].text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 201,
   "id": "b375a874",
   "metadata": {},
   "outputs": [],
   "source": [
    "class NamTien:\n",
    "    def __init__(self):\n",
    "        self.dctUrlProduct = {}\n",
    "        \n",
    "    def getAllUrlTypeProduct(self, urlType, numberOfPages):\n",
    "        lstUrlPruct = []\n",
    "        for i in range(1, numberOfPages):\n",
    "            urlPage = urlType + \"?page=\"+ str(i)\n",
    "            page = requests.get(urlPage)\n",
    "            soup = BeautifulSoup(page.text, 'html.parser')\n",
    "            for div_pro in soup.find_all(class_='product'):\n",
    "                urlProduct = div_pro.a['href']\n",
    "                lstUrlPruct.append(urlProduct)\n",
    "        self.dctUrlProduct[urlType]=lstUrlPruct\n",
    "    def getAllInforProduct(self):\n",
    "        lstALLInforProuct = []\n",
    "        for k,v in self.dctUrlProduct.items():\n",
    "            \n",
    "            for nameProduct in v:\n",
    "                urlPage = \"https://xemaynamtien.com/\" + nameProduct\n",
    "                page = requests.get(urlPage)\n",
    "                soup = BeautifulSoup(page.text, 'html.parser')\n",
    "                try:\n",
    "                    title = soup.h1.text\n",
    "                    price = soup.find(class_=\"price-detail\").text\n",
    "                    price = price.replace('\\n','')\n",
    "                    view = soup.find_all(class_ = 'col-md-6')[-1].find_all('p')[-1].text\n",
    "                    lstALLInforProuct.append([k,\"https://xemaynamtien.com/\"+nameProduct, title, price, view])\n",
    "                except:\n",
    "                    continue\n",
    "        return lstALLInforProuct"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 202,
   "id": "37eb4864",
   "metadata": {},
   "outputs": [],
   "source": [
    "namtien  = NamTien()\n",
    "namtien.getAllUrlTypeProduct(\"https://xemaynamtien.com/xe-tay-ga\", 6)\n",
    "namtien.getAllUrlTypeProduct(\"https://xemaynamtien.com/xe-tay-con\",2)\n",
    "namtien.getAllUrlTypeProduct(\"https://xemaynamtien.com/xe-so\",2)\n",
    "namtien.getAllUrlTypeProduct(\"https://xemaynamtien.com/xe-nhap-khau\",2)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 203,
   "id": "f009fa9f",
   "metadata": {},
   "outputs": [],
   "source": [
    "a = namtien.getAllInforProduct()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "id": "214572ad",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 204,
   "id": "f7a5420f",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame(a, columns=['url_1', 'url_2', 'tiêu đề', 'giá', 'lượt xem'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 205,
   "id": "bf518d3e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>url_1</th>\n",
       "      <th>url_2</th>\n",
       "      <th>tiêu đề</th>\n",
       "      <th>giá</th>\n",
       "      <th>lượt xem</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>https://xemaynamtien.com/xe-tay-ga</td>\n",
       "      <td>https://xemaynamtien.com/honda-sh-350i-abs</td>\n",
       "      <td>Honda SH 150i ABS</td>\n",
       "      <td>113,000,000đ</td>\n",
       "      <td>Lượt xem: 3430</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>https://xemaynamtien.com/xe-tay-ga</td>\n",
       "      <td>https://xemaynamtien.com/honda-sh-150i-cbs-tie...</td>\n",
       "      <td>Honda SH 150i CBS Tiêu Chuẩn - Màu Đen, Đỏ</td>\n",
       "      <td>99,000,000đ</td>\n",
       "      <td>Lượt xem: 1434</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>https://xemaynamtien.com/xe-tay-ga</td>\n",
       "      <td>https://xemaynamtien.com/yamaha-grande-ban-gio...</td>\n",
       "      <td>Yamaha Grande Bản Giới Hạn - Màu Cam</td>\n",
       "      <td>49,500,000đ50,000,000đ</td>\n",
       "      <td>Lượt xem: 2547</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>https://xemaynamtien.com/xe-tay-ga</td>\n",
       "      <td>https://xemaynamtien.com/honda-vario-160-cbs-2022</td>\n",
       "      <td>Honda Vario 160 CBS 2022</td>\n",
       "      <td>49,000,000đ51,000,000đ</td>\n",
       "      <td>Lượt xem: 7972</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>https://xemaynamtien.com/xe-tay-ga</td>\n",
       "      <td>https://xemaynamtien.com/honda-vario-160-abs-2022</td>\n",
       "      <td>Honda Vario 160 ABS 2022</td>\n",
       "      <td>55,000,000đ60,000,000đ</td>\n",
       "      <td>Lượt xem: 14801</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>121</th>\n",
       "      <td>https://xemaynamtien.com/xe-nhap-khau</td>\n",
       "      <td>https://xemaynamtien.com/honda-vario-125-khoa-...</td>\n",
       "      <td>Honda Vario 125 (Khóa Thường Không ISS)</td>\n",
       "      <td>43,000,000đ46,000,000đ</td>\n",
       "      <td>Lượt xem: 3021</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>122</th>\n",
       "      <td>https://xemaynamtien.com/xe-nhap-khau</td>\n",
       "      <td>https://xemaynamtien.com/suzuki-satria-nhap-khau</td>\n",
       "      <td>Suzuki Satria Nhập Khẩu</td>\n",
       "      <td>51,500,000đ</td>\n",
       "      <td>Lượt xem: 2005</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>123</th>\n",
       "      <td>https://xemaynamtien.com/xe-nhap-khau</td>\n",
       "      <td>https://xemaynamtien.com/suzuki-raider-the-thao</td>\n",
       "      <td>Suzuki Raider Thể Thao</td>\n",
       "      <td>50,500,000đ</td>\n",
       "      <td>Lượt xem: 1820</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>124</th>\n",
       "      <td>https://xemaynamtien.com/xe-nhap-khau</td>\n",
       "      <td>https://xemaynamtien.com/suzuki-raider-tieu-chuan</td>\n",
       "      <td>Suzuki Raider Tiêu Chuẩn</td>\n",
       "      <td>49,800,000đ</td>\n",
       "      <td>Lượt xem: 2562</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>125</th>\n",
       "      <td>https://xemaynamtien.com/xe-nhap-khau</td>\n",
       "      <td>https://xemaynamtien.com/yamaha-mx-king</td>\n",
       "      <td>Yamaha MX King</td>\n",
       "      <td>52,000,000đ</td>\n",
       "      <td>Lượt xem: 3106</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>126 rows × 5 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                                     url_1  \\\n",
       "0       https://xemaynamtien.com/xe-tay-ga   \n",
       "1       https://xemaynamtien.com/xe-tay-ga   \n",
       "2       https://xemaynamtien.com/xe-tay-ga   \n",
       "3       https://xemaynamtien.com/xe-tay-ga   \n",
       "4       https://xemaynamtien.com/xe-tay-ga   \n",
       "..                                     ...   \n",
       "121  https://xemaynamtien.com/xe-nhap-khau   \n",
       "122  https://xemaynamtien.com/xe-nhap-khau   \n",
       "123  https://xemaynamtien.com/xe-nhap-khau   \n",
       "124  https://xemaynamtien.com/xe-nhap-khau   \n",
       "125  https://xemaynamtien.com/xe-nhap-khau   \n",
       "\n",
       "                                                 url_2  \\\n",
       "0           https://xemaynamtien.com/honda-sh-350i-abs   \n",
       "1    https://xemaynamtien.com/honda-sh-150i-cbs-tie...   \n",
       "2    https://xemaynamtien.com/yamaha-grande-ban-gio...   \n",
       "3    https://xemaynamtien.com/honda-vario-160-cbs-2022   \n",
       "4    https://xemaynamtien.com/honda-vario-160-abs-2022   \n",
       "..                                                 ...   \n",
       "121  https://xemaynamtien.com/honda-vario-125-khoa-...   \n",
       "122   https://xemaynamtien.com/suzuki-satria-nhap-khau   \n",
       "123    https://xemaynamtien.com/suzuki-raider-the-thao   \n",
       "124  https://xemaynamtien.com/suzuki-raider-tieu-chuan   \n",
       "125            https://xemaynamtien.com/yamaha-mx-king   \n",
       "\n",
       "                                        tiêu đề                     giá  \\\n",
       "0                             Honda SH 150i ABS            113,000,000đ   \n",
       "1    Honda SH 150i CBS Tiêu Chuẩn - Màu Đen, Đỏ             99,000,000đ   \n",
       "2          Yamaha Grande Bản Giới Hạn - Màu Cam  49,500,000đ50,000,000đ   \n",
       "3                      Honda Vario 160 CBS 2022  49,000,000đ51,000,000đ   \n",
       "4                      Honda Vario 160 ABS 2022  55,000,000đ60,000,000đ   \n",
       "..                                          ...                     ...   \n",
       "121     Honda Vario 125 (Khóa Thường Không ISS)  43,000,000đ46,000,000đ   \n",
       "122                     Suzuki Satria Nhập Khẩu             51,500,000đ   \n",
       "123                      Suzuki Raider Thể Thao             50,500,000đ   \n",
       "124                    Suzuki Raider Tiêu Chuẩn             49,800,000đ   \n",
       "125                              Yamaha MX King             52,000,000đ   \n",
       "\n",
       "            lượt xem  \n",
       "0     Lượt xem: 3430  \n",
       "1     Lượt xem: 1434  \n",
       "2     Lượt xem: 2547  \n",
       "3     Lượt xem: 7972  \n",
       "4    Lượt xem: 14801  \n",
       "..               ...  \n",
       "121   Lượt xem: 3021  \n",
       "122   Lượt xem: 2005  \n",
       "123   Lượt xem: 1820  \n",
       "124   Lượt xem: 2562  \n",
       "125   Lượt xem: 3106  \n",
       "\n",
       "[126 rows x 5 columns]"
      ]
     },
     "execution_count": 205,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 215,
   "id": "c9eeb2f3",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['giá niêm yết'] = df['giá'].apply(lambda row: row.split('đ')[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 217,
   "id": "f7e0f424",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['giá gốc'] = df['giá'].apply(lambda row: row.split('đ')[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 225,
   "id": "2263161e",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.drop('giá', inplace=True, axis =1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 227,
   "id": "bc730aab",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_csv('data_namtien.xlsx', sep=';')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 219,
   "id": "3ea55459",
   "metadata": {},
   "outputs": [],
   "source": [
    "namtien  = NamTien()\n",
    "namtien.getAllUrlTypeProduct(\"https://xemaynamtien.com/cac-mau-dang-giam-gia\", 2)\n",
    "giamgia = namtien.getAllInforProduct()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 220,
   "id": "ed4c28a0",
   "metadata": {},
   "outputs": [],
   "source": [
    "df2 = pd.DataFrame(giamgia, columns=['url_1', 'url_2', 'tiêu đề ', 'giá', 'lượt xem'])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 221,
   "id": "5c2cf648",
   "metadata": {},
   "outputs": [],
   "source": [
    "df2['giá niêm yết'] = df2['giá'].apply(lambda row: row.split('đ')[0])\n",
    "df2['giá gốc'] = df2['giá'].apply(lambda row: row.split('đ')[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 226,
   "id": "f14ed36a",
   "metadata": {},
   "outputs": [],
   "source": [
    "df2.drop('giá', inplace = True, axis =1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 228,
   "id": "0b8431f9",
   "metadata": {},
   "outputs": [],
   "source": [
    "df2.to_csv('data_namtien_giamgia.xlsx',sep=\";\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 224,
   "id": "97d9796d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(16, 7)"
      ]
     },
     "execution_count": 224,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2.shape"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
