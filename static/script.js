$(document).ready(function () {

    $("#solveBtn").click(function () {

        let a = $("#a").val();
        let b = $("#b").val();
        let c = $("#c").val();

        // basic validation
        if (a === "" || b === "" || c === "") {
            $("#output").html(
                "<div class='alert alert-warning'>Please fill all inputs</div>"
            );
            return;
        }

        $.ajax({
            url: "/solve",
            type: "GET",
            data: { a: a, b: b, c: c },

            success: function (response) {

                $("#output").html(`
                    <div class="alert alert-success">
                        <h5>${response.result.type}</h5>
                        <p><b>Root 1:</b> ${response.result.root1}</p>
                        <p><b>Root 2:</b> ${response.result.root2}</p>
                        <hr>
                        <p><b>Server IP:</b> ${response.server_ip}</p>
                    </div>
                `);

            },

            error: function () {
                $("#output").html(
                    "<div class='alert alert-danger'>Server error</div>"
                );
            }
        });

    });

});