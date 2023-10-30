package main

import (
	_ "GoSimpleDB/src/utils/sqlman"
	_ "fmt"
	"image/color"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/canvas"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/theme"
	"fyne.io/fyne/v2/widget"
)

const WINDOW_TITLE string = "GoSimpleDB"
const DEF_PRJ_TAB_NAME string = "Новый проект*"

var DEF_WiN_SIZE fyne.Size = fyne.NewSize(1280, 720)
var DEF_THEME fyne.Theme = theme.DarkTheme()
var PNL_BG_CLR []color.Color = []color.Color{color.RGBA{16, 27, 43, 255}, color.RGBA{92, 139, 209, 175}}

var prjch chan *project_data = make(chan *project_data)
var tabch chan *container.TabItem = make(chan *container.TabItem, 1)
var crtbfrch chan int = make(chan int, 1)
var crtwndch chan *create_tabel_window = make(chan *create_tabel_window, 1)

var m_a fyne.App = init_app()

type window_data struct {
	window fyne.Window

	content struct {
		empty_screen *fyne.Container
		main_m       *main_menu
		tab          *container.DocTabs
		prjs         []*project_data
		crt_wnd      *create_tabel_window
	}
}

type create_tabel_window struct {
	window    fyne.Window
	root      *window_data
	root_page *project_data

	content struct {
		body *fyne.Container
	}
}

type main_menu struct {
	menu fyne.MainMenu

	sub_menus []fyne.Menu
}

type project_data struct {
	root    *container.DocTabs
	tab     *container.TabItem
	tbl_doc *container.DocTabs

	body *fyne.Container

	tool_panel struct {
		panel  *fyne.Container
		pnl_bg *canvas.Rectangle
		tools  []*fyne.Container
		wdgts  map[*fyne.Container][]*fyne.Widget
	}
}

func main() {

	w_st := init_window(m_a)
	crtbfrch = nil
	//close(crtbfrch)

	go func() {
		for w_st.window != nil {
			if len(w_st.content.tab.Items) > 0 && w_st.window.Content() == w_st.content.empty_screen {
				w_st.window.SetContent(w_st.content.tab)
				w_st.window.Content().Refresh()
			} else if len(w_st.content.tab.Items) == 0 && w_st.window.Content() != w_st.content.empty_screen {
				w_st.window.SetContent(w_st.content.empty_screen)
				w_st.window.Content().Refresh()
			}
		}
	}()

	go func(ch <-chan *create_tabel_window) {
		for w_st.window != nil {
			if crt := <-ch; w_st.content.crt_wnd == nil {
				w_st.content.crt_wnd = crt
				w_st.content.crt_wnd.window.SetCloseIntercept(
					func() {
						w_st.content.crt_wnd.window.Close()
						w_st.content.crt_wnd.window = nil
						w_st.content.crt_wnd = nil
						//w_st.content.crt_wnd = nil
					},
				)
				w_st.content.crt_wnd.window.CenterOnScreen()
				w_st.content.crt_wnd.window.Show()
			}

			if w_st.content.crt_wnd != nil && w_st.content.crt_wnd.window != nil {
				if w_st.content.crt_wnd.root_page == nil {
					w_st.content.crt_wnd.window.Close()
					w_st.content.crt_wnd.window = nil
					w_st.content.crt_wnd = nil
				}
			}
		}
	}(crtwndch)

	go func(ch <-chan *project_data) {
		for w_st.window != nil {
			if ch != nil {
				if crtbfrch != nil {
					if p := <-ch; p != nil {
						w_st.content.prjs = append(w_st.content.prjs, p)
						//println("\nprj len: ", len(w_st.content.prjs))
						w_st.content.tab.Append(p.tab)
						println("\nTab add")
						crtbfrch <- len(w_st.content.tab.Items)
					}
				}
			}
		}
	}(prjch)

	go func() {
		for w_st.window != nil {
			if crtbfrch != nil {
				println(crtbfrch)
				<-crtbfrch
				crtbfrch = nil
				println(crtbfrch)
			} else {
				if len(w_st.content.prjs) > len(w_st.content.tab.Items) {
					println(len(w_st.content.prjs), " - ", len(w_st.content.tab.Items))

					if len(w_st.content.tab.Items) == 0 && len(w_st.content.prjs) > 0 {
						w_st.content.prjs = nil
						w_st.content.prjs = []*project_data{}
						println("lens now: ", len(w_st.content.prjs), " - ", len(w_st.content.tab.Items))
					}

					for i, iv := range w_st.content.prjs {
						key := 0
						for _, jv := range w_st.content.tab.Items {
							if iv.tab != jv {
								key++
							} else {
								key = 0
								break
							}
						}

						if key == len(w_st.content.tab.Items) {
							if iv.tab == w_st.content.tab.Selected() {
								w_st.content.tab.OnUnselected(iv.tab)
							}
							w_st.content.prjs = append(w_st.content.prjs[:i], w_st.content.prjs[i+1:]...)
							println("lens now: ", len(w_st.content.prjs), " - ", len(w_st.content.tab.Items))
							println(w_st.content.crt_wnd)
						}
					}
				}
			}
		}
	}()

	//go func() {
	//	for w_st.window != nil {
	//
	//	}
	//}()

	go func(ch chan<- *container.TabItem) {
		for w_st.window != nil {
			if w_st.content.tab.Selected() != nil {

				ch <- w_st.content.tab.Selected()
			}
		}
	}(tabch)

	go func(ch <-chan *container.TabItem) {
		for w_st.window != nil {
			cur_tab := <-ch
			if cur_tab != nil {
				do_resize_tab_cont(&w_st, cur_tab)
			}
		}
	}(tabch)

	w_st.window.SetMaster()
	w_st.window.Show()
	m_a.Run()
}

func init_app() fyne.App {
	a := app.New()
	a.Settings().SetTheme(DEF_THEME)

	return a
}

func init_window(a fyne.App) window_data {
	w_st := window_data{
		window: a.NewWindow(WINDOW_TITLE),
	}
	w_st.window.Resize(DEF_WiN_SIZE)

	w_st.content.empty_screen = container.NewCenter(widget.NewLabel("Добро пожаловать в " + WINDOW_TITLE))
	w_st.content.main_m = init_main_menu(&w_st)
	w_st.window.SetMainMenu(&w_st.content.main_m.menu)
	w_st.content.tab = container.NewDocTabs()
	w_st.content.prjs = []*project_data{}

	return w_st
}

func init_main_menu(w_st *window_data) *main_menu {
	fl := *fyne.NewMenu(
		"Файл",
		fyne.NewMenuItem(
			"Создать проект",
			func() {
				println("\nStart create a tab")
				println(crtbfrch)
				go create_new_project(w_st, prjch)
			},
		),
		fyne.NewMenuItem(
			"Открыть проект",
			nil,
		),
		fyne.NewMenuItem(
			"Удалить проект",
			nil,
		),
		fyne.NewMenuItemSeparator(),
		fyne.NewMenuItem(
			"Выход",
			nil,
		),
	)

	fl.Items[len(fl.Items)-1].IsQuit = true
	fl.Items[1].ChildMenu = fyne.NewMenu("", fyne.NewMenuItem("Все проекты...", nil))

	mn := main_menu{
		sub_menus: []fyne.Menu{
			fl,
		},
	}
	mn.menu = *fyne.NewMainMenu(&mn.sub_menus[0])
	return &mn
}

func init_tool_panel(w_st *window_data, prj *project_data) []*fyne.Container {

	crt_tbl := *widget.NewButton(
		"Создать таблицу",
		func() {
			create_crt_tbl_wnd(w_st, w_st.content.tab.Selected(), crtwndch)
		},
	)
	o_tbl := *widget.NewButton(
		"Открыть таблицу",
		nil,
	)
	dlt_tbl := *widget.NewButton(
		"Удалить таблицу",
		nil,
	)

	tools := []*fyne.Container{
		container.NewCenter(
			widget.NewLabel("Таблица"),
		),
		container.NewGridWithColumns(
			2,
			&crt_tbl,
			&o_tbl,
			&dlt_tbl,
		),
	}
	//wdgts := make(map[*fyne.Container][]*fyne.Widget)

	return tools
}

func create_new_project(w_st *window_data, ch chan<- *project_data) {
	println("\nCreatin' process")
	prj := project_data{}
	prj.root = w_st.content.tab
	prj.tool_panel.pnl_bg = canvas.NewRectangle(color.Alpha{})
	prj.tool_panel.tools = init_tool_panel(w_st, &prj)
	prj.tool_panel.panel = container.NewVBox()
	for i, _ := range prj.tool_panel.tools {
		prj.tool_panel.panel.Add(prj.tool_panel.tools[i])
	}

	prj.body = container.NewWithoutLayout(prj.tool_panel.pnl_bg, prj.tool_panel.panel)

	prj.tab = container.NewTabItem(
		DEF_PRJ_TAB_NAME,
		prj.body,
	)

	prj.tbl_doc = container.NewDocTabs()
	prj.tbl_doc.SetTabLocation(container.TabLocationBottom)

	println("\nSending project")
	if crtbfrch == nil {
		crtbfrch = make(chan int, 1)
	}
	println(crtbfrch, "\n")
	ch <- &prj
}

func create_crt_tbl_wnd(w_st *window_data, tab *container.TabItem, ch chan<- *create_tabel_window) {
	crt_st := create_tabel_window{
		window: m_a.NewWindow(WINDOW_TITLE + "- Создание таблицы"),
		root:   w_st,
	}

	for _, v := range w_st.content.prjs {
		if tab == v.tab {
			crt_st.root_page = v
		}
	}

	crt_st.window.Resize(fyne.NewSquareSize(600))
	crt_st.window.SetFixedSize(true)

	ch <- &crt_st
}

func do_resize_tab_cont(w_st *window_data, tab *container.TabItem) {
	//println("\ntab in resize: ", tab)
	//tab.Content.Resize(w_st.content.tab.Size())

	var prj *project_data
	for i, _ := range w_st.content.prjs {
		if tab == w_st.content.prjs[i].tab {
			prj = w_st.content.prjs[i]
			break
		}
	}
	prj.tool_panel.pnl_bg.Resize(fyne.NewSize(320, tab.Content.Size().Height-10))
	prj.tool_panel.panel.Resize(fyne.NewSize(300, tab.Content.Size().Height-20))
	prj.tool_panel.panel.Move(fyne.NewPos(10, 10))
	prj.tool_panel.pnl_bg.Move(fyne.NewPos(0, 5))
	prj.tool_panel.pnl_bg.StrokeColor = color.RGBA{75, 76, 77, 150}
	prj.tool_panel.pnl_bg.FillColor = color.RGBA{75, 76, 77, 150}
	prj.tool_panel.pnl_bg.StrokeWidth = 1.5
	prj.tool_panel.pnl_bg.CornerRadius = 10
	//println("\nprjs len: ", len(w_st.content.prjs))
}
