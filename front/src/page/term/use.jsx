import { useNavigate, Link } from "react-router-dom";
import * as React from "react";

import './term.css';
export default function UseTerm() {
    return (
        <body className="d-flex flex-column h-100">
            <main className="flex-shrink-0">
                <section className="get-started section-bg">
                    <div className="container">
                        <h2 className="display-5 fw-bolder" style={{ marginBottom: '50px' }}>
                        <span className="text-gradient d-inline">이용약관</span>
                        <p className='notice-text'>LawABLE의 이용약관을 확인해보세요.</p>
                        </h2>

                        <div style={{textAlign:'left', margin:'auto'}}>
                            <p className="content-subtitle">제 1 조 (목적)</p>
                            
                            <p>이 약관에서 사용하는 주요 용어의 정의는 다음과 같습니다.</p>

                            <p> “서비스”라 함은 구현되는 단말기와 상관 없이 “이용자”가 이용할 수 있는 LawABLE 관련 제반 서비스를 의미합니다.
                            <br/>“이용자”란 이 약관에 따라 “회사”가 제공하는 “서비스”를 받는 “회원” 및 “비회원”을 말합니다.
                            <br/>“회원”이란 “회사”의 서비스를 이용하기 위하여 이용약관에 동의 및 필요한 정보를 등록하고 회사가 제공하는 서비스를 이용하는 자를 말합니다. 
                            <br/>“회원”은 개인회원, 기업회원, 변호사회원으로 구분합니다.
                           
                            <br/>“아이디(ID)”라 함은 “회원”의 식별과 “서비스” 이용을 위하여 “회원”이 정하고 “회사”가 승인하는 문자 또는 문자와 숫자의 조합을 의미합니다.
                            <br/>"비밀번호”라 함은 “회원”이 부여받은 “아이디”와 일치되는 “회원”임을 확인하고 비밀의 보호를 위해 “회원” 자신이 정한 문자(특수문자 포함)와 숫자의 조합을 의미합니다.
                            </p>
                            <br/>
                            <br/>
                        

                            <p className="content-subtitle">제 2 조 (약관의 게시와 개정)</p>
                            <p>“회사”는 본 약관의 내용과 상호 및 대표자 성명, 영업소 소재지 주소(“이용자”의 불만을 처리할 수 있는 곳의 주소를 포함), 전화번호·전자우편주소, 사업자등록번호, 통신판매업 신고번호, 개인정보관리책임자 등을 “이용자”가 쉽게 알 수 있도록 “웹사이트 등”의 초기 서비스화면(전면)에 게시하고 약관의 중요한 내용을 굵은 문자 등으로 명확하게 표시합니다. 다만, 약관의 내용은 “이용자”가 연결화면을 통하여 볼 수 있도록 할 수 있습니다.</p>
                            <p>“회사”는 “약관의규제에관한법률”, “정보통신망이용촉진및정보보호등에관한법률 (이하 “정보 통신망법”)” 등 관련 법을 위배하지 않는 범위에서 이 약관을 개정할 수 있습니다.</p>
                            <p>“회사”가 약관을 개정할 경우에는 적용일자 및 개정내용을 명시하여 현행약관과 함께 7일 이전부터 적용일자 전일까지 사이트 초기화면에 공지하며, 변경된 내용은 “이용자”가 연결화면을 통하여 볼 수 있도록 할 수 있습니다. 전자이메일이 등록된 회원에게 전자메일을 통하여 공지합니다. 다만, “회원”에게 불리하게 약관 내용을 변경하는 경우에는 최소한 30일 이상의 사전유예 기간을 두고 공지합니다. 이 경우 “회사”는 약관의 개정 전 내용과 개정 후 내용을 명확하게 비교하여 “회원”이 알기 쉽도록 표시합니다.</p>
                            <p>“회사”가 전항에 따라 개정 약관을 공지 또는 통지하면서 “회원”에게 30일 기간 내에 의사 표시를 하지 않으면 의사표시가 표명된 것으로 본다는 뜻을 명확하게 공지 또는 통지하였음에도 회원이 명시적으로 거부의 의사표시를 하지 아니한 경우 “회원”이 개정약관에 동의한 것으로 봅니다.</p>
                            <p> “회원”이 개정약관의 적용에 동의하지 않는 경우 “회사”는 개정 약관의 내용을 적용할 수 없습니다. 이 경우 “회사”는 “회원”에게 기존 약관을 적용하거나, 개정 약관의 적용의 유예기간을 둘 수 있으며, “회원”은 이용 계약을 해지할 수 있습니다. 다만, “회사”가 다른 “회원”과의 형평성의 적용 문제 등 기존 약관을 적용할 수 없는 특별한 사정이 있는 경우에는 “회사”는 이용계약을 해지할 수 있습니다.</p>
                            
                            <br/>
                            <br/>

                            <p className="content-subtitle">제 3 조 (약관의 해석)</p>
                            <p>“회사”는 “유료서비스” 및 개별 서비스에 대해서는 별도의 이용약관 및 정책(이하 “유료서비스약관 등”)을 둘 수 있으며, 해당 내용이 이 약관과 상충할 경우에는 “유료서비스약관 등”이 우선하여 적용됩니다.</p>
                            <p>이 약관에서 정하지 아니한 사항이나 해석에 대해서는 “유료서비스약관 등” 및 관계법령 또는 상관례에 따릅니다.</p>
                            
                            <br/>
                            <br/>

                            <p className="content-subtitle">제 4 조 (개인정보보호 의무)</p>
                            <p>“회사”는 “개인정보보호법” 등 관계 법령이 정하는 바에 따라 “회원”의 개인정보를 보호하기 위해 노력합니다. 개인정보의 보호 및 사용에 대해서는 관련 법 및 “회사”의 개인정보처리방침이 적용됩니다. 다만, “회사”에서 운영하는 웹 사이트 등에서 링크된 사이트에서는 “회사”의 개인정보처리방침이 적용되지 않습니다.</p>

                            <br/>
                            <br/>

                            <p className="content-subtitle">제 5 조 (“회원”의 “아이디” 및 “비밀번호”의 관리에 대한 의무)</p>
                            <p>“회원”의 “아이디”와 “비밀번호”에 관한 관리책임은 “회원”에게 있으며, 이를 제3자가 이용하도록 하여서는 안 됩니다.</p>
                            <p>“회사”는 “회원”의 “아이디”가 개인정보 유출 우려가 있거나, 반사회적 또는 미풍양속에 어긋나거나 “회사” 및 “회사”의 운영자로 오인한 우려가 있는 경우, 해당 “아이디”의 이용 을 제한할 수 있습니다.</p>
                            <p>“회원”은 “아이디” 및 “비밀번호”가 도용되거나 제3자가 사용하고 있음을 인지한 경우에는 이를 즉시 “회사”에 통지하고 “회사”의 안내에 따라야 합니다.</p>
                            <p>제3항의 경우에 해당 “회원”이 “회사”에 그 사실을 통지하지 않거나, 통지한 경우에도 “회사”의 안내에 따르지 않아 발생한 불이익에 대하여 “회사”는 책임지지 않습니다.</p>

                            <br/>
                            <br/>

                            <p className="content-subtitle">제 8 조 (“회원”에 대한 통지)</p>
                            <p>“회사”가 “회원”에 대한 통지를 하는 경우 이 약관에 별도 규정이 없는 한 “회사”의 계정이나 전화번호 등을 발신인으로 한 회원의 전자우편, 문자메시지, 전자쪽지, 그 외 회사의 웹 사이트 등을 통한 게시로 할 수 있습니다.</p>
                        
                        </div>
                    </div>
                </section>
            </main>
        </body>
    );
}
