



var dialogInstace , onMoveStartId , mousePos = {x:0,y:0};	//	���ڼ�¼��ǰ����ק�Ķ���

	// var zIndex = 9000;

	//	��ȡԪ�ض���
	function g(id){return document.getElementById(id);}

	//	�Զ�����Ԫ�أ�el = Element��
	function autoCenter( el ){
		var bodyW = document.documentElement.clientWidth;
		var bodyH = document.documentElement.clientHeight;

		var elW = el.offsetWidth;
		var elH = el.offsetHeight;

		el.style.left = (bodyW-elW)/2 + 'px';
		el.style.top = (bodyH-elH)/2 + 'px';

	}

	//	�Զ���չԪ�ص�ȫ����ʾ����
	function fillToBody( el ){
		el.style.width  = document.documentElement.clientWidth  +'px';
		el.style.height = document.documentElement.clientHeight + 'px';
	}

	//	Dialogʵ�����ķ���
	function Dialog( dragId , moveId ){

		var instace = {} ;

		instace.dragElement  = g(dragId);	//	����ִ�� ��ק���� ��Ԫ��
		instace.moveElement  = g(moveId);	//	��ק����ʱ���ƶ���Ԫ��

		instace.mouseOffsetLeft = 0;			//	��ק����ʱ���ƶ�Ԫ�ص���ʼ X ��
		instace.mouseOffsetTop = 0;			//	��ק����ʱ���ƶ�Ԫ�ص���ʼ Y ��

		instace.dragElement.addEventListener('mousedown',function(e){

			var e = e || window.event;

			dialogInstace = instace;
			instace.mouseOffsetLeft = e.pageX - instace.moveElement.offsetLeft ;
			instace.mouseOffsetTop  = e.pageY - instace.moveElement.offsetTop ;

			onMoveStartId = setInterval(onMoveStart,10);
			return false;
			// instace.moveElement.style.zIndex = zIndex ++;
		})

		return instace;
	}

	//	��ҳ�������� ��굯���¼�
	document.onmouseup = function(e){

		dialogInstace = false;
		clearInterval(onMoveStartId);
	}
	document.onmousemove = function( e ){
		var e = window.event || e;
		mousePos.x = e.clientX;
		mousePos.y = e.clientY;


		e.stopPropagation && e.stopPropagation();
		e.cancelBubble = true;
		e = this.originalEvent;
        e && ( e.preventDefault ? e.preventDefault() : e.returnValue = false );

        document.body.style.MozUserSelect = 'none';
	}

	function onMoveStart(){


		var instace = dialogInstace;
	    if (instace) {

	    	var maxX = document.documentElement.clientWidth -  instace.moveElement.offsetWidth;
	    	var maxY = document.documentElement.clientHeight - instace.moveElement.offsetHeight ;

			instace.moveElement.style.left = Math.min( Math.max( ( mousePos.x - instace.mouseOffsetLeft) , 0 ) , maxX) + "px";
			instace.moveElement.style.top  = Math.min( Math.max( ( mousePos.y - instace.mouseOffsetTop ) , 0 ) , maxY) + "px";

	    }

	}





	//	���µ����Ի����λ�ú����֣�����չ��
	function showDialog(){
		g('dialogMove').style.display = 'block';
		g('mask').style.display = 'block';
		autoCenter( g('dialogMove') );
		fillToBody( g('mask') );


	}

	//	�رնԻ���
	function hideDialog(){
		g('dialogMove').style.display = 'none';
		g('mask').style.display = 'none';
	}

	//	������������ڴ�С�仯
	// window.onresize = showDialog;

	Dialog('dialogDrag','dialogMove');

	//Ĭ�����õ���������
	// showDialog();

    function quanxuan(){//û�е���jquery
    	var item=document.getElementsByName("item")
		// item.prop("checked",true)
		for (i=0;i<item.length;i++){
			item[i].checked=true
		}

	}

	function fanxuan(){//û�е���jquery
    	var item=document.getElementsByName("item")
		// item.prop("checked",true)
		for (i=0;i<item.length;i++){
			if(item[i].checked) {

                item[i].checked = false
            }
			else{
				item[i].checked = true
			}
		}

	}

	function mycommit(){//û�е���jquery
    	var stuid=document.getElementById("stuid").innerText
		checkvalue=[]
    	var item=document.getElementsByName("item")
		for (i=0;i<item.length;i++){
			if(item[i].checked){
				checkvalue.push(item[i].value);
			}
		}
        mydata={"stuid":stuid,"mychecked":"hereis checked"}
        $.post(
        	"/shenhe/",
			JSON.stringify({"stuid":stuid,"mychecked":checkvalue}),
			function(data){
			},
			"json"
			);
        hideDialog()
		heretr=window.heretr
		heretr.remove()
		// heretr.parentNode.removeChild(heretr)

	}



	function gezhi(stuid){
        $.post(
        	"/gezhi/",
			JSON.stringify({"stuid":stuid}),
			function(data){

			},
			"json"
			);
        heretr=window.heretr
        heretr.remove()

		//tbody=$(document.getElementsByTagName("tbody")[0])


	}

	function butongguo(stuid){
    	$.post(
        	"/butongguo/",
			JSON.stringify({"stuid":stuid}),
			function(data){

			},
			"json"
			);
        heretr=window.heretr
        heretr.remove()
	}

	//��ʱˢ�½��棨0.5�룩

