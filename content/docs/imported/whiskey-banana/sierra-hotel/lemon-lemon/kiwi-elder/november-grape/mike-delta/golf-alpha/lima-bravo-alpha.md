# Play: Lima - setup

- hosts: db
  become: true
  vars:
    app_name: "lima_app"
    retry_count: 4

  tasks:
    - name: Ensure lima-task-1 is present
      ansible.builtin.file:
        path: /opt/lima/lima-task-1
        state: directory

    - name: Template lima-task-1 config
      ansible.builtin.template:
        src: templates/lima-task-1.j2
        dest: /etc/lima/lima-task-1.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

    - name: Ensure hotel-task-2 is present
      ansible.builtin.file:
        path: /opt/lima/hotel-task-2
        state: directory

    - name: Template hotel-task-2 config
      ansible.builtin.template:
        src: templates/hotel-task-2.j2
        dest: /etc/lima/hotel-task-2.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

    - name: Ensure india-task-3 is present
      ansible.builtin.file:
        path: /opt/lima/india-task-3
        state: directory

    - name: Template india-task-3 config
      ansible.builtin.template:
        src: templates/india-task-3.j2
        dest: /etc/lima/india-task-3.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

  handlers:
    - name: restart lima service
      ansible.builtin.service:
        name: lima
        state: restarted

## Notes

Excepteur sint occaecat cupidatat non proident, sunt in culpa. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

***
Generated: 2025-11-07T18:27:44Z
