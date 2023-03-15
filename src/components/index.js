import AppBreadcrumb from './AppBreadcrumb'
import AppContent from './AppContent'
import AppFooter from './AppFooter'
import AppHeader from './AppHeader'
import AppHeaderDropdown from './header/AppHeaderDropdown'
import AppSidebar from './AppSidebar'
import DocsCallout from './DocsCallout'
import DocsLink from './DocsLink'
import DocsExample from './DocsExample'
import App from './FileBrowser'
import { setChonkyDefaults } from 'chonky'
import { ChonkyIconFA } from 'chonky-icon-fontawesome'
setChonkyDefaults({ iconComponent: ChonkyIconFA })
export {
  AppBreadcrumb,
  AppContent,
  AppFooter,
  AppHeader,
  AppHeaderDropdown,
  AppSidebar,
  DocsCallout,
  DocsLink,
  DocsExample,
  App,
}
