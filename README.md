- Đây là một trang thương mại điện tử đơn giản là bán đồ thời trang nhưng vẫn đầy đủ các chức năng như : bán , mua , cart , login , logout, register,..

----Note: Đây là một sàn giao dịch đơn giản nên sẽ không có lợi nhuận cho admin :v

- Sử dụng công nghệ Django (Framework của python) - công nghệ chính, sử dụng thêm các framework khác như jquery , bootstrap , tailwindcss để xử lí font-end

- "puddle" là thư mục gốc , các thư mục khác là các app chức năng


- Bán : Mỗi người muốn bán đồ thì sẽ phải tạo một acc để đăng đồ mình muốn bán
    +) Mục "New Item" sẽ thực hiện chức năng này
    +) Mỗi item sẽ có các thuộc tính là : id ,name , description , category , price , image , created_by , create_at, is_sold , remaining_quantity(Số lượng hàng có tồn )
        - Id: django đã mặc định tự tạo
- Edit :
    +) Khi người bán muốn chỉnh sửa thông tin về sản phẩm như số lượng hàng tồn , tên , giới thiệu,... mỗi item sẽ có chức năng edit (Chức năng này chỉ khi login và là item của minh mới thực hiện được)
- Mua :
    +) Ý tưởng: khi muốn mua một món đồ thì họ sẽ phải qua bước checkout: điền thông tin địa chỉ, số điện thoại người nhận , số lượng. Khi đã hoàn thành thì yêu cầu sẽ được gửi về người bán và người bán xác nhận thông qua việc liên lạc với người mua. Người bán và người mua tự thỏa thuận với nhau về phương thức thanh toán cũng như vận chuyển

- Cart : phần giỏ hàng chúng ta có thể thêm, xóa các món đồ đã chọn 

- Inbox: người bán và người mua có thể liên lạc với nhau qua tin nhắn về món đồ đã chọn

- Feedback: Người mua có thể để lại feed back sau khi đã mua và nhận được sản phẩm cũng như xem được các feedback người mua khác đăng tải

-Có các models chính : User , Item , Category , Cart , Conversation , Order