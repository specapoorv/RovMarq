import pandas as pd
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex, QFileSystemWatcher

class csvFileComponent(QAbstractTableModel):
    def __init__(self, csv_path, parent=None):
        super().__init__(parent)
        self.csv_path = csv_path
        self._data = pd.read_csv(csv_path)
        
        # Setup file watcher for real-time updates
        self.watcher = QFileSystemWatcher([csv_path])
        self.watcher.fileChanged.connect(self.reload_data)
    
    def reload_data(self):
        self._data = pd.read_csv(self.csv_path)
        self.layoutChanged.emit()
        
        if self.csv_path not in self.watcher.files():
            self.watcher.addPath(self.csv_path)
    
    def rowCount(self, parent=QModelIndex()):
        if parent == QModelIndex():
            return len(self._data)
        return 0
    
    def columnCount(self, parent=QModelIndex()):
        if parent == QModelIndex():
            return len(self._data.columns)
        return 0
    
    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.EditRole:
            return str(self._data.iloc[index.row(), index.column()])
        return None
    
    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self._data.columns[section])
            if orientation == Qt.Orientation.Vertical:
                return str(section + 1)
        return None
    
    def flags(self, index):
        if not index.isValid():
            return Qt.ItemFlag.NoItemFlags
        return (
            Qt.ItemFlag.ItemIsSelectable 
            | Qt.ItemFlag.ItemIsEnabled 
            | Qt.ItemFlag.ItemIsEditable
        )

    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            # Update the DataFrame
            self._data.iloc[index.row(), index.column()] = value
            
            # Notify the view
            self.dataChanged.emit(index, index, [role])
            
            # Save back to CSV
            self._data.to_csv(self.csv_path, index=False)
            
            return True
        return False
